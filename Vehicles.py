import arcade
import math

from controls import on_key_press, on_key_release  # Import the on_key_press and on_key_release functions
import VehicleBody as vb

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BAR_WIDTH = 100
BAR_HEIGHT = 10

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bar and Circles")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.bar = vb.Bar(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BAR_WIDTH, BAR_HEIGHT)

        # Create a sprite list and add the bar and circles
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.bar)
        self.sprite_list.append(self.bar.circle1)
        self.sprite_list.append(self.bar.circle2)

        # Create a moving sprite
        self.moving_sprite = arcade.Sprite("sprites/hobo.png", 2.0)
        #self.moving_sprite = arcade.Sprite(":resources:images/enemies/fly.png", 0.5)
        self.moving_sprite.center_x = 100
        self.moving_sprite.center_y = 100
        self.moving_sprite.change_x = 0.2
        self.sprite_list.append(self.moving_sprite)

        # Track keys pressed
        self.keys_pressed = set()

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def on_update(self, delta_time):
        # Update the sprite list
        self.sprite_list.update()

        # Update the bar based on keys pressed
        if arcade.key.A in self.keys_pressed:
            self.bar.move(-10, 0)
        if arcade.key.D in self.keys_pressed:
            self.bar.move(10, 0)
        if arcade.key.W in self.keys_pressed:
            self.bar.move(0, 10)
        if arcade.key.S in self.keys_pressed:
            self.bar.move(0, -10)
        if arcade.key.Q in self.keys_pressed:
            self.bar.rotate(5)
        if arcade.key.E in self.keys_pressed:
            self.bar.rotate(-5)

    def on_key_press(self, key, modifiers):
        on_key_press(key, modifiers, self.keys_pressed)  # Call the imported function with the keys_pressed set

    def on_key_release(self, key, modifiers):
        on_key_release(key, modifiers, self.keys_pressed)  # Call the imported function with the keys_pressed set

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
