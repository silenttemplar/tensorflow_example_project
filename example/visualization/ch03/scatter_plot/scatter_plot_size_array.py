import matplotlib.pyplot as plt
import numpy as np

def data2size(data, min_size, max_size):
    data_copy = data.copy()

    min_val = np.min(data_copy)
    data_copy -= min_val

    max_val = np.max(data_copy)
    data_copy = data_copy / max_val

    interval = max_size - min_size
    data_copy *= interval
    data_copy += min_size
    return data_copy

if __name__ == '__main__':
    print('dataset_utils.py')

    n_data = 10
    x_data = np.linspace(0, 10, n_data)
    y_data = np.linspace(0, 10, n_data)

    z_data = np.random.normal(0, 1, n_data)
    s_arr = data2size(z_data, 100, 2000)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(x_data, y_data, s=s_arr)

    plt.show()