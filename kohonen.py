from customsom import MiniSom
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import os
import datagen
import plot

def generate_data(fig, data_n):
    if fig == 'grid':
        return datagen.generate_grid(data_n)
    elif fig == 'circle':
        return datagen.generate_circle(data_n)
    elif fig == 'triangle':
        return datagen.generate_triangle(data_n)
    elif fig == 'random-circle':
        return datagen.generate_random_circle(data_n)


def plot_data(fig, reference_points, points, data_n, draw_lines, filename):
    return plot.plot_figure(reference_points, points, data_n, draw_lines, filename)


def apply_kohonen(n, it, data_n, fig, draw_lines = False):
    # Generating the data
    X = generate_data(fig, data_n)
    # Initi the som
    som = MiniSom(x=n, y=n, input_len=2, sigma=1.0, learning_rate=0.5)
    som.random_weights_init(X)
    som.train_random(data=X, num_iteration=it, verbose=False)
    # Create folders
    # Checking the directory
    folders = f'results/{n}-{it}-{data_n}-{fig}'
    if not os.path.isdir(folders):
        # If the directory is not present then create it.
        os.makedirs(folders)
    # Iterate som
    for i in range(it):
        som.train_step()
        plot_data(fig, X, som.get_weights(), data_n, draw_lines, f'{folders}/{i}.jpg')
    
    
