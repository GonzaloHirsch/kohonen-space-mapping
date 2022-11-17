import numpy as np
import random

def generate_grid(data_n):
    # Expect data_n to be a perfect square
    size = int(np.sqrt(data_n))
    # Create an X and Y set
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    return np.array([[_x, _y] for _y in y for _x in x])

def generate_circle(data_n, radius = 1):
    delta = np.pi * 2 / (data_n)
    return np.array([[np.cos(p * delta) * radius , np.sin(p * delta) * radius ] for p in range(data_n)])

def generate_random_circle(data_n, radius = 1):
    origin = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
    points = []

    while (len(points) != data_n):
        point = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
        if np.linalg.norm(point - origin) < radius:
            points.append(point)
    return np.array(points)

def generate_triangle(data_n, radius = 1):
    sides = data_n // 3
    bottom = data_n // 3 + (data_n % 3)
    side_l_x = np.linspace(-radius, 0, sides + 1)[1:]
    side_l_y = radius + side_l_x
    side_r_x = np.linspace(0, radius, sides + 1)[1:]
    side_r_y = radius - side_r_x
    side_b_x = np.linspace(-radius, radius, bottom + 1)
    side_b_y = np.zeros(bottom)
    x = np.concatenate([side_l_x, side_r_x, side_b_x])
    y = np.concatenate([side_l_y, side_r_y, side_b_y])
    return np.array([[x[p], y[p]] for p in range(data_n)])

