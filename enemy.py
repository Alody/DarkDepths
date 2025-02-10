import pygame
from constants import *
import random

walking_anim = pygame.image.load("assets/Characters(100x100)/Orc/Orc/Orc-Walk.png")

walking_frames = []
for i in range(SPRITE_COLUMNS):
    frame = walking_anim.subsurface(pygame.Rect(i * SPRITE_FRAME_WIDTH, 0, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT))
    frame = pygame.transform.scale(frame, (int(SPRITE_FRAME_WIDTH * SPRITE_SCALE), int(SPRITE_FRAME_HEIGHT * SPRITE_SCALE)))
    walking_frames.append(frame)


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = walking_frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > ANIMATION_SPEED:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the edges of the screen
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.speed_y = -self.speed_y

