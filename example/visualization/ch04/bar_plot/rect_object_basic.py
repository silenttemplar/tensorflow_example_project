import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 10
data = np.random.uniform(10, 20, (n_data, ))

data_idx = np.arange(n_data)
data_labels = np.array(['class '+str(i) for i in range(n_data)])

fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=15)

y_ticks = ax.get_yticks()
ytick_interval = y_ticks[1] - y_ticks[0]
ax.set_ylim([0, 20 + ytick_interval*0.5])

rects = ax.bar(data_idx, data,
               hatch='/',
               facecolor='whitesmoke',
               edgecolor='silver')

for rect_idx, rect in enumerate(rects):
    x = rect.get_x()
    width = rect.get_width()
    height = rect.get_height()

    ax.text(x + width/2, height+ytick_interval*0.2,
            s=str(round(data[rect_idx])),
            #rotation=90,
            ha='center', fontsize=15)

ax.set_xticks(data_idx)
ax.set_xticklabels(data_labels, rotation=30)
ax.grid(axis='y')

plt.show()
