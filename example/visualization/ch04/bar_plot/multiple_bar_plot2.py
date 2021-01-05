import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 10

background = 50 * np.ones(n_data)
data1 = np.random.uniform(20, 40, (n_data, ))
data2 = np.random.uniform(10, 20, (n_data, ))

data_idx = np.arange(n_data)
colors = ['tab:blue', 'tab:red']

fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=15)

ax.bar(data_idx, background,
       hatch='/',
       facecolor='whitesmoke',
       edgecolor='silver')

rects1 = ax.bar(data_idx, data1,
                color='tab:blue',
                label=colors[0])
rects2 = ax.bar(data_idx, data2,
                color='tab:red',
                label=colors[1])

y_ticks = ax.get_yticks()
ytick_interval = y_ticks[1] - y_ticks[0]
#ax.set_ylim([0, 50 + ytick_interval*0.5])

for rect_idx, rect in enumerate(rects1):
    x = rect.get_x()
    width = rect.get_width()
    height = rect.get_height()

    ax.text(x + width/2, height+ytick_interval*0.2,
            s=str(round(height)),
            rotation=90,
            ha='left',
            fontsize=20,
            color=colors[0])

for rect_idx, rect in enumerate(rects2):
    x = rect.get_x()
    width = rect.get_width()
    height = rect.get_height()

    ax.text(x + width/2, height+ytick_interval*0.2,
            s=str(round(height)),
            rotation=90,
            ha='right',
            fontsize=20,
            color=colors[1])

ax.grid(axis='y')
plt.legend()

plt.show()
