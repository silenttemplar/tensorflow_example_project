import matplotlib.pyplot as plt

from example.visualization.ch02.dataset.bop_utils import get_year_data, bop_data_reader

def bop_plot(dataset, t_year, ax):
    t_year_data = get_year_data(dataset, t_year)
    ax.plot(t_year_data[:,-1], label='Year '+str(t_year))

if __name__ == '__main__':
    dataset = bop_data_reader('../dataset/BrentOilPrices.csv')
    fig, ax = plt.subplots(figsize=(10, 7))

    bop_plot(dataset, 90, ax)
    bop_plot(dataset, 93, ax)
    bop_plot(dataset, 96, ax)

    ax.set_title('BOP data')
    ax.set_ylabel('daily prices in USD')

    ax.grid()
    ax.legend(loc='upper left')

    plt.show()
