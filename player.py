from ursina import *

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'quad'
        self.texture = 
        self.scale_y = 2
        self.speed = 5
        self.health = 100
        self.armor = 10



        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.y += held_keys['w'] * time.dt * self.speed
        self.y -= held_keys['s'] * time.dt * self.speed