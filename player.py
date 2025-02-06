from ursina import *

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'quad'
        self.texture = 'base char/idle.png'  # Sprite sheet
        self.color = color.white
        self.scale_y = 2
        self.speed = 5
        self.health = 100
        self.armor = 10

        # Sprite sheet properties
        self.frame = 0
        self.frames_per_row = 4  # Number of columns
        self.frames_per_column = 3  # Number of rows
        self.total_frames = self.frames_per_row * self.frames_per_column

        # Set proper texture scaling
        self.texture_scale = Vec2(1 / self.frames_per_row, 1 / self.frames_per_column)

        self.update_uvs()

        for key, value in kwargs.items():
            setattr(self, key, value)
            
        # Trigger animation on movement
        if held_keys['d'] or held_keys['a'] or held_keys['w'] or held_keys['s']:
            self.animate_sprite()

    def update_uvs(self):
        row = self.frame // self.frames_per_row
        column = self.frame % self.frames_per_row
        self.texture_offset = Vec2(column / self.frames_per_row, 1 - (row + 1) / self.frames_per_column)

    def animate_sprite(self):
        self.frame = (self.frame + 1) % self.total_frames
        self.update_uvs()
