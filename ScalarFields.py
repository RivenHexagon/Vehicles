import math
import constants as c

def gaussian(x, y, amplitude, x0, y0, sigma_x, sigma_y):
    return amplitude * math.exp(-((x - x0) ** 2 / (2 * sigma_x ** 2) + (y - y0) ** 2 / (2 * sigma_y ** 2)))

def temperature_field(x, y):
    heat_source1 = gaussian(x, y, 192, c.SCREEN_WIDTH * 0.75, c.SCREEN_HEIGHT * 0.75, 150, 150)
    heat_source2 = gaussian(x, y, 192, c.SCREEN_WIDTH * 0.40 , c.SCREEN_HEIGHT * 0.25, 150, 150)
    return heat_source1 + heat_source2