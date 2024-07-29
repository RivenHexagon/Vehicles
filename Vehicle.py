import arcade
import math

from ScalarFields import gaussian
from VehicleBrains import *
import constants as c


class VehicleBody(arcade.SpriteSolidColor):
    def __init__(self, world, start_pos, width, height):
        super().__init__(width, height, c.VEHICLE_COLOR)
        self.center_x = start_pos[0]
        self.center_y = start_pos[1]
        self.angle = 0
        self.world = world
        self.sensorRigOffset = c.SENSOR_RIG_OFFSET
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self)
        self.sensorRig = SensorRig(start_pos[0], start_pos[1] + self.sensorRigOffset, c.SENSOR_DIST, self.world.temperature)
        self.sprite_list.extend(self.sensorRig.sprite_list)

        self.brain = VehicleBrain2(self)
        self.driver = Driver(self)

        self.angle_text = arcade.Text(
            "angle text",
            self.center_x, self.center_y,
            arcade.color.BLACK,
            10,
            anchor_x="center",
            anchor_y="center",
            rotation=self.angle
            )
        self.trail = []

    def rotate(self, delta_angle):
        self.angle += delta_angle
        self.update()

    def move(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y
        self.update()

    def update(self):
        super().update()
        self.brain.update()
        angle_radians = math.radians(self.angle)
        offset_x = self.sensorRigOffset * math.sin(angle_radians)
        offset_y = self.sensorRigOffset * math.cos(angle_radians)
        self.sensorRig.center_x = self.center_x - offset_x
        self.sensorRig.center_y = self.center_y + offset_y
        self.sensorRig.angle = self.angle
        self.sensorRig.update()
        self.angle_text.x = self.center_x
        self.angle_text.y = self.center_y
        #self.rotating_text.rotation = self.angle
        self.angle_text.text = f"{self.angle:.1f}"
        #self.brain.update()
        self.trail.append((self.center_x, self.center_y))
        if len(self.trail) > c.TRAIL_LENGTH:
            self.trail.pop(0)

    def draw_trail(self):
        # Draw the trail
        if len(self.trail) > 1:
            arcade.draw_line_strip(self.trail, (48, 160, 48), 2)

class SensorRig(arcade.SpriteSolidColor):
    def __init__(self, x, y, senDist, scalar_field):
        super().__init__(senDist, c.SENSOR_RIG_WIDTH, c.SENSOR_RIG_COLOR)
        self.center_x = x
        self.center_y = y
        self.angle = 0
        self.sensorDistance = senDist
        self.leftSensor  = Sensor(scalar_field, self.center_x + self.sensorDistance / 2, self.center_y, c.CIRCLE_RADIUS)
        self.rightSensor = Sensor(scalar_field, self.center_x - self.sensorDistance / 2, self.center_y, c.CIRCLE_RADIUS)
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

        self.leftSensor.update()
        self.rightSensor.update()


class Sensor(arcade.SpriteCircle):
    def __init__(self, scalar_field, x, y, radius):
        super().__init__(radius, (192,32,32))
        self.scalar_field = scalar_field
        self.center_x = x
        self.center_y = y
        self.radius = radius
        self.value = 0
        self.value_text = arcade.Text(
            "value text",
            self.center_x, self.center_y,
            arcade.color.BLACK,
            10,
            anchor_x="center",
            anchor_y="center",
            rotation=0.0
            )
    
    def update(self):
        self.update_text()
        self.update_color()

    def update_text(self):
        self.value_text.text = f"{self.value:.1f}"
        self.value_text.x = self.center_x
        self.value_text.y = self.center_y

    def update_color(self):
        self.value = self.scalar_field(self.center_x, self.center_y)
        color_intensity = int(self.value)
        self.color = (c.FIELD_AMPLITUDE, color_intensity, color_intensity)
        # Update texture with new color
        self.texture = arcade.make_circle_texture(self.radius * 2, self.color) 


class Driver:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def setSpeed(self, speed):
        angle_rad = math.radians(self.vehicle.angle)
        vel_x = -speed * math.sin(angle_rad)
        vel_y = speed * math.cos(angle_rad)
        self.vehicle.velocity = (vel_x, vel_y)
    
    def steer(self, rot_speed):
        self.vehicle.angle += rot_speed