import pygame
import sys
import os
from settings import *
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Load and play background music
        self.main_sound = self.load_sound('audio', 'main.ogg', volume=0.5)
        if self.main_sound:
            self.main_sound.play(loops=-1)
    
    def load_sound(self, *path, volume=1.0):
        """Load a sound file, ensure the path is correct, and set the volume."""
        full_path = os.path.join(*path)
        try:
            sound = pygame.mixer.Sound(full_path)
            sound.set_volume(volume)
            return sound
        except pygame.error as e:
            print(f"Error loading sound: {full_path} - {e}")
            return None

    def run(self):
        while True:
            self.handle_events()
            self.update_screen()
            self.clock.tick(FPS)
    
    def handle_events(self):
        """Handle all game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

    def handle_keydown(self, event):
        """Handle keydown events."""
        if event.key == pygame.K_m:
            self.level.toggle_menu()

    def update_screen(self):
        """Update the game screen."""
        self.screen.fill(WATER_COLOR)
        self.level.run()
        pygame.display.update()

    def quit_game(self):
        """Quit the game safely."""
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
