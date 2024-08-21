import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = self.load_animation_frames()

    def load_animation_frames(self):
        """Load all animation frames into a dictionary."""
        frames = {
            # Magic animations
            'flame': self.load_frames('graphics/particles/flame/frames'),
            'aura': self.load_frames('graphics/particles/aura'),
            'heal': self.load_frames('graphics/particles/heal/frames'),
            
            # Attack animations
            'claw': self.load_frames('graphics/particles/claw'),
            'slash': self.load_frames('graphics/particles/slash'),
            'sparkle': self.load_frames('graphics/particles/sparkle'),
            'leaf_attack': self.load_frames('graphics/particles/leaf_attack'),
            'thunder': self.load_frames('graphics/particles/thunder'),

            # Monster death animations
            'squid': self.load_frames('graphics/particles/smoke_orange'),
            'raccoon': self.load_frames('graphics/particles/raccoon'),
            'spirit': self.load_frames('graphics/particles/nova'),
            'bamboo': self.load_frames('graphics/particles/bamboo'),
            
            # Leaf animations
            'leaf': self.load_leaf_frames()
        }
        return frames

    def load_frames(self, path):
        """Load frames from a given path."""
        return import_folder(path)

    def load_leaf_frames(self):
        """Load and reflect leaf frames."""
        leaf_paths = [
            'graphics/particles/leaf1',
            'graphics/particles/leaf2',
            'graphics/particles/leaf3',
            'graphics/particles/leaf4',
            'graphics/particles/leaf5',
            'graphics/particles/leaf6'
        ]
        leaf_frames = []
        for path in leaf_paths:
            original_frames = self.load_frames(path)
            reflected_frames = self.reflect_images(original_frames)
            leaf_frames.extend([original_frames, reflected_frames])
        return tuple(leaf_frames)

    def reflect_images(self, frames):
        """Reflect frames horizontally."""
        return [pygame.transform.flip(frame, True, False) for frame in frames]

    def create_grass_particles(self, pos, groups):
        """Create grass particles effect."""
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        """Create a particle effect for a given animation type."""
        animation_frames = self.frames.get(animation_type)
        if animation_frames:
            ParticleEffect(pos, animation_frames, groups)
        else:
            print(f"Animation type '{animation_type}' not found.")


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        """Animate the particle effect by updating the frame index."""
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        """Update the particle effect."""
        self.animate()
