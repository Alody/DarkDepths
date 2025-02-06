from ursina import *
from player import Player

# Initialize the game
app = Ursina()

# Create the player
player = Player()

# Create a simple menu
def start_game():
    print("Game Started!")
    menu.enabled = False

menu = Entity(parent=camera.ui, enabled=True)
Text("Dark Depths", parent=menu, scale=2, y=0.3)
Button("Start", scale=(0.2, 0.1), y=0, on_click=start_game, parent=menu)
Button("Quit", scale=(0.2, 0.1), y=-0.15, on_click=application.quit, parent=menu)

# Run the game
app.run()
