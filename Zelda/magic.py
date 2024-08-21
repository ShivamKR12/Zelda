import pygame
from settings import *
from random import randint
import os

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': self.load_sound('audio', 'heal.wav'),
            'flame': self.load_sound('audio', 'Fire.wav')
        }

    def load_sound(self, *path):
        """Load a sound file, ensuring the path is correct and the file exists."""
        full_path = os.path.join(*path)
        try:
            return pygame.mixer.Sound(full_path)
        except pygame.error as e:
            print(f"Error loading sound: {full_path} - {e}")
            return None

    def play_sound(self, sound_key):
        """Safely play a sound if it was loaded successfully."""
        sound = self.sounds.get(sound_key)
        if sound:
            sound.play()

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.play_sound('heal')
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center, groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.play_sound('flame')

            # Determine direction based on player's status
            direction = self.get_direction(player.status)

            for i in range(1, 6):
                if direction.x:  # Horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)
                else:  # Vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x, y), groups)

    def get_direction(self, status):
        """Get the direction vector based on player's status."""
        if status.split('_')[0] == 'right':
            return pygame.math.Vector2(1, 0)
        elif status.split('_')[0] == 'left':
            return pygame.math.Vector2(-1, 0)
        elif status.split('_')[0] == 'up':
            return pygame.math.Vector2(0, -1)
        else:
            return pygame.math.Vector2(0, 1)
