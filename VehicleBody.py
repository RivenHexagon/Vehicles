import arcade
import math
from ScalarFields import gaussian

CIRCLE_RADIUS = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Bar(arcade.SpriteSolidColor):
    def __init__(self, x, y, width, height):
        super().__init__(width, height, (48,48,48))
        self.center_x = x
        self.center_y = y
        self.angle = 0

        # Calculate the initial positions of the circles
        self.circle1 = Circle(self.center_x + width / 2, self.center_y, CIRCLE_RADIUS)
        self.circle2 = Circle(self.center_x - width / 2, self.center_y, CIRCLE_RADIUS)

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
    def __init__(self, x, y, radius):
        super().__init__(radius, (192,32,32))
        self.center_x = x
        self.center_y = y
        self.radius = radius

    def update_color(self):
        value = gaussian(self.center_x, self.center_y, 255, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 150, 150)
        color_intensity = int(value)
        print(color_intensity)
        print(self.color)
        self.color = (192, color_intensity, color_intensity)
        self.texture = arcade.make_circle_texture(self.radius * 2, self.color)  # Update texture with new color