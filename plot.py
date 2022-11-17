import numpy as np
import matplotlib.pyplot as plt


def draw_relation_lines(size, shaped_points):
    for x in range(size):
        for y in range(size):
            _x, _y = [], []
            if y + 1 < size:
                _x.append(shaped_points[x, y][0])
                _y.append(shaped_points[x, y][1])
                _x.append(shaped_points[x, y + 1][0])
                _y.append(shaped_points[x, y + 1][1])
            if y - 1 >= 0:
                _x.append(shaped_points[x, y][0])
                _y.append(shaped_points[x, y][1])
                _x.append(shaped_points[x, y - 1][0])
                _y.append(shaped_points[x, y - 1][1])
            if x + 1 < size:
                _x.append(shaped_points[x, y][0])
                _y.append(shaped_points[x, y][1])
                _x.append(shaped_points[x + 1, y][0])
                _y.append(shaped_points[x + 1, y][1])
            if x - 1 >= 0:
                _x.append(shaped_points[x, y][0])
                _y.append(shaped_points[x, y][1])
                _x.append(shaped_points[x - 1, y][0])
                _y.append(shaped_points[x - 1, y][1])
            plt.plot(_x, _y, '-r', label="Kohonen")

def plot_figure(reference_points, points, data_n, draw_lines, filename):
    # Expect data_n to be a perfect square
    size = int(np.sqrt(data_n))
    # Reshape to be in matrix form
    shape = (size, size, 2)
    shaped_points = points.reshape(shape)
    # Iterate and plot all connections for each point
    plt.clf()
    plt.scatter(reference_points[:, 0],
                reference_points[:, 1], c='b', marker='s', label="Target")
    # Draw the kohonen points
    if draw_lines:
        draw_relation_lines(size, shaped_points)
    else:
        _x = shaped_points[:, :, 0]
        _y = shaped_points[:, :, 1]
        plt.scatter(_x, _y, c='red', label="Kohonen")
    plt.axis('off')
    plt.axis('equal')
    plt.legend()
    plt.savefig(filename)
