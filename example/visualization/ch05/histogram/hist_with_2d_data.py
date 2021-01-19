import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_class = 2
n_data = 300
colors= ['b', 'r']

# example 1
data = np.random.normal(0, 1, (n_data, n_class))

fig, ax = plt.subplots()
freqs, bin_edges, rects = ax.hist(data)

bin_center = (bin_edges[:-1] + bin_edges[1:]) / 2
ax.set_xticks(bin_center)
ax.set_xticklabels(np.around(bin_center, 2), rotation=30)

ylim = ax.get_ylim()
ax.set_ylim([ylim[0], ylim[1]+10])

# histogram 내 수치표현
for class_idx in range(n_class):
    color = colors[class_idx]

    for rect in rects[class_idx]:
        x = rect.get_x()
        width = rect.get_width()
        height = rect.get_height()
        ax.text(x + width/2, height+2, str(height), rotation=90, ha='center', color=color)

# example 2
'''
data1 = np.random.normal(0, 1, (n_data, 1))
data2 = np.random.normal(-5, 2, (n_data, 1))
data3 = np.random.normal(5, 3, (n_data, 1))
data = np.hstack((data1, data2, data3))
print('data.shape: {}'.format(data.shape))

fig, ax = plt.subplots()
freqs, bin_edges, rects = ax.hist(data, bins=30,
                                  label=['data1','data2','data3'],
                                  color=['coral', 'royalblue', 'purple'])
print('freqs.shape: {}'.format(freqs.shape))
print('bin_edges.shape: {}'.format(bin_edges.shape))
print('rects: {}'.format(rects))
ax.legend()
'''

plt.show()
