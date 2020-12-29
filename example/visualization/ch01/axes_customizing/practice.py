import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# example 1
'''
axes_g1 = np.empty(shape=(0,))
main1 = plt.subplot2grid((5,4), (0,0), rowspan=2, colspan=2, fig=fig)
main1.get_xaxis().set_visible(False)
main1.get_yaxis().set_visible(False)
axes_g1 = np.append(axes_g1, main1)

for row in range(2, 2 + 3):
    for col in range(2):
        sub_ax = plt.subplot2grid((5, 4), (row, col), fig=fig)
        axes_g1 = np.append(axes_g1, sub_ax)

axes_g1 = axes_g1.reshape(1, -1)
print('axes_g1.shape: {}'.format(axes_g1.shape))

axes_g2 = np.empty(shape=(0,))
main2 = plt.subplot2grid((5,4), (0,2), rowspan=2, colspan=2, fig=fig)
main2.get_xaxis().set_visible(False)
main2.get_yaxis().set_visible(False)
axes_g2 = np.append(axes_g2, main2)

for row in range(2, 2 + 3):
    for col in range(2, 2 + 2):
        sub_ax = plt.subplot2grid((5, 4), (row, col), fig=fig)
        axes_g2 = np.append(axes_g2, sub_ax)

axes_g2 = axes_g2.reshape(1, -1)
print('axes_g2.shape: {}'.format(axes_g2.shape))

# axes 병합
axes = np.vstack((axes_g1, axes_g2))
#axes = np.hstack((axes_g1, axes_g2))
print('axes.shape: {}'.format(axes.shape))
'''

# example 2
axes = np.empty(shape=(0, 7))
for g_idx in range(2):
    axes_g = np.empty(shape=(0,))

    main = plt.subplot2grid((5, 4), (0, 2*g_idx), rowspan=2, colspan=2, fig=fig)
    axes_g = np.append(axes_g, main)

    for row in range(2, 2 + 3):
        for col in range(2):
            sub_ax = plt.subplot2grid((5, 4), (row, col+2*g_idx), fig=fig)
            axes_g = np.append(axes_g, sub_ax)

    axes_g = axes_g.reshape(1, -1)
    axes = np.vstack((axes, axes_g))

print('axes.shape: {}'.format(axes.shape))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

fig.subplots_adjust(bottom=0.03, top=0.97, left=0.03, right=0.97)
fig.subplots_adjust(hspace=0, wspace=0)

plt.show()

