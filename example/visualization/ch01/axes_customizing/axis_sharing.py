import matplotlib.pyplot as plt

# method 1

fig, axes = plt.subplots(nrows=2, ncols=2,
                         figsize=(7, 7),
                         sharex=True,
                         sharey=True)
axes[0, 0].set_xlim([0, 100])
axes[0, 0].set_ylim([0, 1])

# method 2
'''
fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2, sharey=ax1)
ax3 = fig.add_subplot(2, 2, 3, sharex=ax1)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_xlim([0, 10])
ax1.set_ylim([0, 5])
'''

# method 3
'''
fig = plt.figure(figsize=(7, 7))
ax1_1 = plt.subplot2grid((2, 2), (0, 0), fig=fig)
ax1_2 = plt.subplot2grid((2, 2), (0, 1), fig=fig)
ax2_1 = plt.subplot2grid((2, 2), (1, 0), fig=fig)
ax2_2 = plt.subplot2grid((2, 2), (1, 1), fig=fig)
'''

# method 4
'''
left, bottom = 0.1, 0.1
spacing = 0.1
height, width = 0.35, 0.35

rect1 = [left, bottom, width, height]
rect2 = [left+width+spacing, bottom, width, height]
rect3 = [left, bottom+height+spacing, width, height]
rect4 = [left+width+spacing, bottom+height+spacing, width, height]

fig = plt.figure(figsize=(7, 7))
ax1_1 = fig.add_axes(rect1)
ax1_2 = fig.add_axes(rect2, sharey=ax1_1)
ax2_1 = fig.add_axes(rect3, sharex=ax1_1)
ax2_2 = fig.add_axes(rect4, sharex=ax2_1, sharey=ax2_1)

ax1_1.set_ylim([0, 100])
ax2_1.set_ylim([0, 200])
ax1_1.set_xlim([0, 10])
ax1_2.set_xlim([0, 20])
'''
plt.show()