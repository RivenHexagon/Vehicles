import arcade
import math
from ScalarFields import gaussian
import constants as c


class VehicleBody(arcade.SpriteSolidColor):
    def __init__(self, world, x, y, width, height):
        super().__init__(width, height, (128,128,128))
        self.center_x = x
        self.center_y = y
        self.angle = 0
        self.world = world
        self.sensorRigOffset = c.SENSOR_RIG_OFFSET
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self)
        self.sensorRig = SensorRig(x, y + self.sensorRigOffset, c.SENSOR_DIST, world)
        self.sprite_list.extend(self.sensorRig.sprite_list)

    def rotate(self, delta_angle):
        self.angle += delta_angle
        self.update()

    def move(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y
        self.update()

    def update(self):
        #self.sensorRig.center_x = self.center_x
        #self.sensorRig.center_y = self.center_y + self.sensorRigOffset
        angle_radians = math.radians(self.angle)
        offset_x = self.sensorRigOffset * math.sin(angle_radians)
        offset_y = self.sensorRigOffset * math.cos(angle_radians)
        self.sensorRig.center_x = self.center_x - offset_x
        self.sensorRig.center_y = self.center_y + offset_y
        self.sensorRig.angle = self.angle
        self.sensorRig.update()

class SensorRig(arcade.SpriteSolidColor):
    def __init__(self, x, y, senDist, world):
        super().__init__(senDist, 10, (48,48,48))
        self.center_x = x
        self.center_y = y
        self.angle = 0
        self.sensorDistance = senDist
        self.world = world
        self.leftSensor  = Sensor(self.world, self.center_x + self.sensorDistance / 2, self.center_y, c.CIRCLE_RADIUS)
        self.rightSensor = Sensor(self.world, self.center_x - self.sensorDistance / 2, self.center_y, c.CIRCLE_RADIUS)
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self)
        self.sprite_list.append(self.leftSensor)
        self.sprite_list.append(self.rightSensor)

    def update(self):
        angle_radians = math.radians(self.angle)
        half_width = self.sensorDistance / 2

        self.leftSensor.center_x = self.center_x + half_width * math.cos(angle_radians)
        self.leftSensor.center_y = self.center_y + half_width * math.sin(angle_radians)

        self.rightSensor.center_x = self.center_x - half_width * math.cos(angle_radians)
        self.rightSensor.center_y = self.center_y - half_width * math.sin(angle_radians)

        self.leftSensor.update_color()
        self.rightSensor.update_color()

class Sensor(arcade.SpriteCircle):
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
        # Update texture with new color
        self.texture = arcade.make_circle_texture(self.radius * 2, self.color) 
