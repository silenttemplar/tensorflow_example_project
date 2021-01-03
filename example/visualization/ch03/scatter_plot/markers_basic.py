import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

#np.random.seed(0)

# example1
'''
n_data = 200
x_data = np.random.normal(0, 1, (n_data,))
y_data = np.random.normal(1, 1, (n_data,))

fig, ax = plt.subplots(figsize=(5, 5))

ax.scatter(x_data, y_data, s=300,
           facecolor='None',
           edgecolor='tab:blue',
           linewidth=5,
           alpha=0.5)
'''

# example2
n_class = 5
n_data = 30
center_pt = np.random.uniform(-20, 20, (n_class, 2))

cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(n_class)]

data_dict = {'class'+str(i):None for i in range(n_class)}
for class_idx in range(n_class):
    center = center_pt[class_idx]
    x_data = center[0] + 2*np.random.normal(0, 1, (1, n_data))
    y_data = center[0] + 2*np.random.normal(0, 1, (1, n_data))
    data = np.vstack((x_data, y_data))
    data_dict['class'+str(class_idx)] = data

fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(n_class):
    data = data_dict['class'+str(class_idx)]
    ax.scatter(data[0], data[1],
               s=1000,
               label='class'+str(class_idx),
               facecolor='None',
               edgecolor=colors[class_idx],
               linewidth=5,
               alpha=0.5)

ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          fontsize=20,
          ncol=1,
          title='Classes',
          title_fontsize=30)

plt.tight_layout()

plt.show()