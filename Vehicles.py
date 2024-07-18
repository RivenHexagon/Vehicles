# Basic arcade program using objects
# Displays a white window with a blue circle in the middle

# Imports
import arcade
import random

import controls as ctrl

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Homless under the Red Sun"
SCALING = 2.0
RADIUS = 150

# Classes
class SpaceShooter(arcade.Window):
    """Main welcome window
    """
    def __init__(self, _width, _height, _title):
        """Initialize the window
        """
        super().__init__(_width, _height, _title)
        arcade.set_background_color((48,48,48))
        self.enemies_list = arcade.SpriteList()
        self.clouds_list  = arcade.SpriteList()
        self.all_sprites  = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play
        """
        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)
        # Set up the player
        self.player = arcade.Sprite("sprites/player.png", SCALING)
        self.player.center_y = 100#self.height / 2
        self.player.left = 100
        #self.player.velocity = (1, 0)
        self.all_sprites.append(self.player)

    def on_key_press(self, symbol, modifiers):
        ctrl.on_key_press(self, symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        ctrl.on_key_release(self, symbol, modifiers)

    def on_draw(self):
        """Called whenever you need to draw your window
        """
        # Clear the screen and start drawing
        arcade.start_render()
        arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.63, RADIUS, (192,32,32))
        self.all_sprites.draw()

    def on_update(self, delta_time: float):
        self.all_sprites.update()

# Main code entry point
if __name__ == "__main__":
    app = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()