import pygame
from constants import *
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dark Depths")

# Create player instance
player = Player(240, 360)
enemy = Enemy(300, 300)
all_sprites = pygame.sprite.Group(player)
all_sprites.add(enemy)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((53, 59, 72))  # Background color (Arsenic)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move_on_command()

    # Update
    all_sprites.update()

    # Draw
    all_sprites.draw(screen)

    # Refresh display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
