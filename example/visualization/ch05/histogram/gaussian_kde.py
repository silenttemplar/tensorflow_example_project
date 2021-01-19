import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(0)

def kde_estimation(data, est_x, n_data, bin_interval):
    estimator = stats.gaussian_kde(data)
    kde = estimator(est_x)
    kde = kde * n_data * bin_interval
    return kde

if __name__ == '__main__':

    # example 1
    '''
    n_data = 300
    data = np.random.normal(0, 1,  (n_data,))
    m_val, M_val = data.min(), data.max()

    estimator_x = np.linspace(m_val, M_val, 100)
    kde_estimator = stats.gaussian_kde(data)
    kde = kde_estimator(estimator_x)

    fig, ax = plt.subplots()

    #freqs, bin_edges, rects = ax.hist(data, alpha=0.5, density=True)
    freqs, bin_edges, rects = ax.hist(data, alpha=0.5)
    bin_interval = bin_edges[1] - bin_edges[0]
    kde = kde * n_data * bin_interval
    ax.plot(estimator_x, kde)
    '''

    # example 2
    n_data_list = [300, 500]
    colors = ['b', 'r']

    data1 = np.random.normal(0, 1,  (n_data_list[0],))
    data2 = np.random.normal(5, 1, (n_data_list[1],))
    data_list = np.array([data1, data2], dtype=object)

    # data 내 min, max 계산
    m_val, M_val = None, None
    for data in data_list:
        if m_val == None or data.min() < m_val:
            m_val = data.min()
        if M_val == None or data.max() > M_val:
            M_val = data.max()

    estimator_x = np.linspace(m_val, M_val, 500)

    fig, ax = plt.subplots()
    
    freqs, bin_edges, rects = ax.hist(data_list, alpha=0.5, color=colors)
    bin_interval = bin_edges[1] - bin_edges[0]
    
    # linear 표현
    for n_data, data, color in zip(n_data_list, data_list, colors):
        K =  kde_estimation(data, estimator_x, n_data, bin_interval)
        ax.plot(estimator_x, K, color=color)
        
    plt.show()