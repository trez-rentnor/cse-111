"""
CSE 111

Author: Randy Jones

"""

# Density of water (without greek letters)
p = 998.2

# Acceleration of gravity
g = 9.80665

def water_column_height(tower_height, tank_height):
    return tower_height + 0.75 * tank_height

def pressure_gain_from_water_height(height):
    return p * g * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return -1 * friction_factor * pipe_length * p * fluid_velocity ** 2 / (2000 * pipe_diameter)