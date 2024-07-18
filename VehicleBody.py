import arcade
import math
from ScalarFields import gaussian
import constants as c


class Vehicle(arcade.SpriteSolidColor):
    def __init__(self, world, x, y, width, height):
        super().__init__(width, height, (48,48,48))
        self.center_x = x
        self.center_y = y
        self.angle = 0
        self.world = world
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self)

       # Calculate the initial positions of the circles
        self.circle1 = Circle(self.world, self.center_x + width / 2, self.center_y, c.CIRCLE_RADIUS)
        self.circle2 = Circle(self.world, self.center_x - width / 2, self.center_y, c.CIRCLE_RADIUS)
        self.sprite_list.append(self.circle1)
        self.sprite_list.append(self.circle2)

    def update(self):
        # Update the circles' positions
        angle_radians = math.radians(self.angle)
        half_width = self.width / 2

        self.circle1.center_x = self.center_x + half_width * math.cos(angle_radians)
        self.circle1.center_y = self.center_y + half_width * math.sin(angle_radians)

        self.circle2.center_x = self.center_x - half_width * math.cos(angle_radians)
        self.circle2.center_y = self.center_y - half_width * math.sin(angle_radians)

        self.circle1.update_color()
        self.circle2.update_color()

    def rotate(self, delta_angle):
        self.angle += delta_angle
        self.update()

    def move(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y
        self.update()

class Circle(arcade.SpriteCircle):
    def __init__(self, world, x, y, radius):
        super().__init__(radius, (192,32,32))
        self.center_x = x
        self.center_y = y
        self.radius = radius
        self.world = world

    def update_color(self):
        value = self.world.temperature(self.center_x, self.center_y, 255, c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2, 150, 150)
        color_intensity = int(value)
        self.color = (192, color_intensity, color_intensity)
        self.texture = arcade.make_circle_texture(self.radius * 2, self.color)  # Update texture with new color