import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

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
    s_arr = np.random.uniform(10, 40, (n_data,))
    data = np.vstack((x_data, y_data, s_arr))
    data_dict['class'+str(class_idx)] = data

fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(n_class):
    data = data_dict['class'+str(class_idx)]
    ax.scatter(data[0], data[1],
               s=data[2]**2,
               label='class'+str(class_idx),
               facecolor='None',
               edgecolor=colors[class_idx],
               linewidth=5,
               alpha=0.5)

ax.legend(loc='lower right',
          fontsize=20,
          ncol=1,
          title='Classes',
          title_fontsize=30)

ax2 = ax.twinx()
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

legend_sizes = [10, 20, 30, 40]
for size_idx, legend_size in enumerate(legend_sizes):
    ax2.scatter([],[],
                facecolor='None',
                edgecolor='Black',
                linewidth=3,
                s=legend_size**2,
                label=str(legend_size))
ax2.legend(loc='center left',
          bbox_to_anchor=(1, 0.5),
          fontsize=20,
          labelspacing=1,
          title='Point Size',
          title_fontsize=30)

plt.tight_layout()

plt.show()