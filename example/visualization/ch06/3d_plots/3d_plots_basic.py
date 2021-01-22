import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

xticks = np.arange(0, 101, 20)
yticks = np.arange(0, 201, 50)
zticks = np.arange(0, 301, 100)

ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticks(zticks)
ax.tick_params(labelsize=20)

ax.set_xlabel('X Axis', fontsize=20, labelpad=20)
ax.set_ylabel('Y Axis', fontsize=20, labelpad=20)
ax.set_zlabel('Z Axis', fontsize=20, labelpad=20)

fig.subplots_adjust(top=1, bottom=0, left=0, right=1)

plt.show()