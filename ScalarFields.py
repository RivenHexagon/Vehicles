import math

def gaussian(x, y, amplitude, x0, y0, sigma_x, sigma_y):
    return amplitude * math.exp(-((x - x0) ** 2 / (2 * sigma_x ** 2) + (y - y0) ** 2 / (2 * sigma_y ** 2)))
