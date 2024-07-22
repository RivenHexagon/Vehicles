import arcade
import math
from PIL import Image
import numpy as np

import constants as c
from controls import on_key_press, on_key_release  # Import the on_key_press and on_key_release functions
import Vehicle as vb
from ScalarFields import temperature_field



class BraitenbergsWorld(arcade.Window):
    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "Vehicles")
        arcade.set_background_color((48,48,48))
        #arcade.set_background_color(arcade.color.SKY_BLUE)
        self.MyVehicle = vb.VehicleBody(self, c.VEHICLE_START, c.SENSOR_DIST, c.VEHICLE_HEIGHT)
        self.temperature = temperature_field

        # Create a sprite list and add the bar and circles
        self.sprite_list = arcade.SpriteList()
        #self.sprite_list.append(self.MyVehicle)
        self.sprite_list.extend(self.MyVehicle.sprite_list)

        # Create a moving sprite
        self.moving_sprite = arcade.Sprite("sprites/hobo.png", 2.0)
        #self.moving_sprite = arcade.Sprite(":resources:images/enemies/fly.png", 0.5)
        self.moving_sprite.center_x = 100
        self.moving_sprite.center_y = 100
        #self.moving_sprite.change_x = 0.2
        self.moving_sprite.velocity = (0.0, 0.0)
        self.sprite_list.append(self.moving_sprite)

        # Track keys pressed
        self.keys_pressed = set()
        self.scalar_field_texture = self.create_scalar_field_texture()

    def create_scalar_field_texture(self):
        width, height = c.SCREEN_WIDTH, c.SCREEN_HEIGHT
        field_data = np.zeros((height, width, 3), dtype=np.uint8)

        for x in range(width):
            for y in range(height):
                value = self.temperature(x, height - y)
                color = (c.FIELD_AMPLITUDE, int(value), int(value))
                field_data[y, x] = color

        image = Image.fromarray(field_data, 'RGB')
        return arcade.Texture("scalar_field", image)

    def on_draw(self):
        arcade.start_render()
        # Visualize the Gaussian field
        #self.draw_scalar_field()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT , self.scalar_field_texture)
        self.sprite_list.draw()

    def draw_scalar_field(self):
        for x in range(0, c.SCREEN_WIDTH, 10):
            for y in range(0, c.SCREEN_HEIGHT, 10):
                value = self.temperature(x,y)
                color = (c.FIELD_AMPLITUDE, int(value), int(value))
                arcade.draw_point(x, y, color, 5)

    def on_update(self, delta_time):
        # Update the sprite list
        self.sprite_list.update()

        # Update the bar based on keys pressed
        if arcade.key.A in self.keys_pressed:
            self.MyVehicle.move(-10, 0)
        if arcade.key.D in self.keys_pressed:
            self.MyVehicle.move(10, 0)
        if arcade.key.W in self.keys_pressed:
            self.MyVehicle.move(0, 10)
        if arcade.key.S in self.keys_pressed:
            self.MyVehicle.move(0, -10)
        if arcade.key.Q in self.keys_pressed:
            self.MyVehicle.rotate(5)
        if arcade.key.E in self.keys_pressed:
            self.MyVehicle.rotate(-5)

    def on_key_press(self, key, modifiers):
        on_key_press(key, modifiers, self.keys_pressed)  # Call the imported function with the keys_pressed set

    def on_key_release(self, key, modifiers):
        on_key_release(key, modifiers, self.keys_pressed)  # Call the imported function with the keys_pressed set

def main():
    game = BraitenbergsWorld()
    arcade.run()

if __name__ == "__main__":
    main()
