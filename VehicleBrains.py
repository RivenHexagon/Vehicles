import math
import constants as c

class VehicleBrain:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def update(self):
        val_left = self.vehicle.sensorRig.leftSensor.value
        val_right = self.vehicle.sensorRig.rightSensor.value

        speed, rot_speed = self.think(val_left, val_right)

        self.vehicle.driver.setSpeed(speed)
        self.vehicle.driver.steer(rot_speed)
        #print("angle", f"{self.vehicle.angle:.2f}", "rot_speed", f"{rot_speed:.2f}", "velocity", f"{self.vehicle.velocity[0]:.2f}", f"{self.vehicle.velocity[1]:.2f}")
    
    def think(self, val_left, val_right):
        speed = (val_left + val_right) / 80
        rot_speed = -1.0 * (val_left - val_right) / 300.0
        return speed, rot_speed

class VehicleBrain2(VehicleBrain):
    def __init__(self, vehicle):
        super().__init__(vehicle)

    def think(self, val_left, val_right):
        act_input = (val_left + val_right) / 2
        #print("act_input:", act_input)
        amplitude = c.MAX_SPEED - c.MIN_SPEED
        speed = self.activation_function(act_input, amplitude, 128, c.SIGMA, c.MIN_SPEED)
        act_input = (val_left - val_right) / 2
        #rot_speed = self.activation_function(act_input, c.MAX_ROT_SPEED, 0, 100)
        rot_speed = -1.0 * (val_left - val_right) / 300.0
        return speed, rot_speed

    def activation_function(self, x, amplitude, x0, sigma_x, offs):
        y = (amplitude * math.exp(-((x - x0) ** 2 / (2 * sigma_x ** 2)))) + offs
        return y
    
