from customsom import MiniSom
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_data(data_n):
    # Expect data_n to be a perfect square
    size = int(np.sqrt(data_n))
    # Create an X and Y set
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    return np.array([[_x, _y] for _y in y for _x in x])


def plot_data(points, data_n, filename):
    # Expect data_n to be a perfect square
    size = int(np.sqrt(data_n))
    # Reshape to be in matrix form
    shape = (size, size, 2)
    shapedPoints = points.reshape(shape)
    # Iterate and plot all connections for each point
    plt.clf()
    for x in range(size):
        for y in range(size):
            _x, _y = [], []
            if y + 1 < size:
                _x.append(shapedPoints[x, y][0])
                _y.append(shapedPoints[x, y][1])
                _x.append(shapedPoints[x, y + 1][0])
                _y.append(shapedPoints[x, y + 1][1])
            if y - 1 >= 0:
                _x.append(shapedPoints[x, y][0])
                _y.append(shapedPoints[x, y][1])
                _x.append(shapedPoints[x, y - 1][0])
                _y.append(shapedPoints[x, y - 1][1])
            if x + 1 < size:
                _x.append(shapedPoints[x, y][0])
                _y.append(shapedPoints[x, y][1])
                _x.append(shapedPoints[x + 1, y][0])
                _y.append(shapedPoints[x + 1, y][1])
            if x - 1 >= 0:
                _x.append(shapedPoints[x, y][0])
                _y.append(shapedPoints[x, y][1])
                _x.append(shapedPoints[x - 1, y][0])
                _y.append(shapedPoints[x - 1, y][1])
            plt.plot(_x, _y, '-r')
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.savefig(filename)


def apply_kohonen(n, it, data_n):
    # Generating the data
    X = generate_data(data_n)
    # Standarizing data
    sc = StandardScaler()
    sc.fit(X)
    X_Scaled = sc.transform(X)
    # Initi the som
    som = MiniSom(x=n, y=n, input_len=2, sigma=1.0, learning_rate=0.5)
    som.random_weights_init(X_Scaled)
    som.train_random(data=X_Scaled, num_iteration=it, verbose=True)
    # Create folders
    # checking if the directory demo_folder2 
    # exist or not.
    folders = f'results/{n}-{it}-{data_n}'
    if not os.path.isdir(folders):
        
        # if the demo_folder2 directory is 
        # not present then create it.
        os.makedirs(folders)
    # Iterate som
    for i in range(it):
        som.train_step()
        plot_data(som.get_weights(), data_n, f'{folders}/{i}.jpg')
    
    
