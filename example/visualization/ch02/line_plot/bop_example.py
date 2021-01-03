import matplotlib.pyplot as plt
import numpy as np
from example.visualization.ch02.dataset.bop_utils import get_year_data, bop_data_reader

def bop_plot(dataset, t_year, ax):
    #t_year_data = get_year_data(dataset, t_year).astype(np.int)
    t_year_data = get_year_data(dataset, t_year)

    month_dict = {m: None for m in range(1, 1 + 12)}
    for data_idx, data in enumerate(t_year_data):
        Y, M, D, price = data
        if month_dict[M] is None:
            month_dict[M] = [data_idx, '-'.join(str(int(i)) for i in [Y, M, D])]

    first_day_label = np.array(list(month_dict.values()))
    x_arange = np.arange(t_year_data.shape[0])

    ax.plot(x_arange, t_year_data[:, -1])

    ax.set_xticks(first_day_label[:,0].astype(np.int))
    ax.set_xticklabels(first_day_label[:, 1], rotation=-30, ha='left')

    ax.set_title("BOP data({})".format(t_year), fontsize=15)
    ax.tick_params(labelsize=20)
    ax.grid()


if __name__ == '__main__':
    t_year_list = [90, 91, 95]
    dataset = bop_data_reader('../dataset/BrentOilPrices.csv')

    fig, axes = plt.subplots(len(t_year_list), 1, figsize=(15, 10))

    for ax_idx, ax in enumerate(axes.flat):
        bop_plot(dataset, t_year_list[ax_idx], ax)

        if ax_idx == 1:
            ax.set_ylabel('daily prices in USD', fontsize=20)

    fig.tight_layout()

    plt.show()