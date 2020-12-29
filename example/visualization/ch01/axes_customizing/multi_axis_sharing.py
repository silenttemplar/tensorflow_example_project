import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 10))
n_row, n_col = 3, 4

axes = np.empty(shape=(0, n_col))
for r_idx in range(n_row):

    axes_row = np.empty(shape=(0, ))

    if r_idx == 0:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, c_idx + (r_idx * n_col) + 1)
            else:
                ax = fig.add_subplot(n_row, n_col, c_idx + (r_idx * n_col) + 1,
                                     sharey=axes_row[0])
            axes_row = np.append(axes_row, ax)
    else:
        for c_idx in range(n_col):
            if c_idx == 0:
                ax = fig.add_subplot(n_row, n_col, c_idx + (r_idx * n_col) + 1,
                                     sharex=axes[0, c_idx])
            else:
                ax = fig.add_subplot(n_row, n_col, c_idx + (r_idx * n_col) + 1,
                                    sharex = axes[0, c_idx],
                                    sharey=axes_row[0])
            axes_row = np.append(axes_row, ax)



    axes = np.vstack((axes, axes_row))
print('axes.shape: {}'.format(axes.shape))

axes[0, 0].set_ylim([0, 100])
axes[1, 0].set_ylim([0, 200])
axes[2, 0].set_ylim([0, 300])

axes[0, 0].set_xlim([0, 10])
axes[0, 1].set_xlim([0, 20])
axes[0, 2].set_xlim([0, 30])
axes[0, 3].set_xlim([0, 40])

fig.tight_layout()
plt.show()