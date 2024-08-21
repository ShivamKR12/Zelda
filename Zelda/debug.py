import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the font (None uses the default font)
try:
    font = pygame.font.Font(None, 30)
except Exception as e:
    print(f"Error initializing font: {e}")
    sys.exit()

def debug(info, y=10, x=10):
    # Get the display surface
    display_surface = pygame.display.get_surface()
    if not display_surface:
        print("Display surface not initialized.")
        return

    # Render the debug information
    try:
        debug_surf = font.render(str(info), True, 'White')
    except Exception as e:
        print(f"Error rendering font: {e}")
        return

    # Get the rectangle of the surface
    debug_rect = debug_surf.get_rect(topleft=(x, y))

    # Draw the rectangle and blit the surface
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)