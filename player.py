import pygame
from constants import *

# Load sprite sheets (idle, walking,)
idle_anim = pygame.image.load("assets/Characters(100x100)/Soldier/Soldier/Soldier-Idle.png")

idle_frames = []
for i in range(SPRITE_COLUMNS):
    frame = idle_anim.subsurface(pygame.Rect(i * SPRITE_FRAME_WIDTH, 0, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT))
    frame = pygame.transform.scale(frame, (int(SPRITE_FRAME_WIDTH * SPRITE_SCALE), int(SPRITE_FRAME_HEIGHT * SPRITE_SCALE)))
    idle_frames.append(frame)

walking_anim = pygame.image.load("assets/Characters(100x100)/Soldier/Soldier/Soldier-Walk.png")

walking_frames = []
for i in range(SPRITE_COLUMNS):
    frame = walking_anim.subsurface(pygame.Rect(i * SPRITE_FRAME_WIDTH, 0, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT))
    frame = pygame.transform.scale(frame, (int(SPRITE_FRAME_WIDTH * SPRITE_SCALE), int(SPRITE_FRAME_HEIGHT * SPRITE_SCALE)))
    walking_frames.append(frame)

# Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = idle_frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()  # Track last frame change time
        self.state = "idle"

    def update(self):
        now = pygame.time.get_ticks()
        
        speed = ANIMATION_SPEED if self.state == "idle" else ANIMATION_SPEED // 2  # 2x faster when walking

        if now - self.last_update > speed:
            self.last_update = now
        
            if self.state == "walking":
                self.frames = walking_frames  # Set frames to walking animation
            else:
                self.frames = idle_frames  # Set frames to idle animation

            # Cycle through the frames
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    
    def move_on_command(self):
        keys = pygame.key.get_pressed()
        moving = False  # Track movement state

        # Allow movement in both X and Y directions simultaneously
        if keys[pygame.K_a]:
            self.rect.x -= 5
            moving = True

        if keys[pygame.K_d]:
            self.rect.x += 5
            moving = True

        if keys[pygame.K_w]:
            self.rect.y -= 5
            moving = True

        if keys[pygame.K_s]:
            self.rect.y += 5
            moving = True

        # Update state
        self.state = "walking" if moving else "idle"
