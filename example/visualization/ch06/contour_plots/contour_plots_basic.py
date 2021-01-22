import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

plt.style.use('seaborn')

# example1
'''
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
levels = np.linspace(Z.min()+0.0001, Z.max(), 50)
'''

# example2
X, Y, Z = get_test_data(0.5)

levels = np.linspace(Z.min()+0.0001, Z.max(), 30)

fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

ax1.plot_wireframe(X, Y, Z)

contour = ax2.contour(X, Y, Z, levels=levels, cmap='hot', linestyles='-.')
contour_zero = ax2.contour(X, Y, Z, levels=0, cmap='Greys', linestyles=':', linewidths=5)

cbar = fig.colorbar(contour, pad=0., fraction=0.15)

label_levels = contour.levels[::2]
ax2.clabel(contour, levels=label_levels)
ax2.clabel(contour_zero, [0], fontsize=20)

ax2.set_xlabel('X coordinate', fontsize=20)
ax2.set_ylabel('Y coordinate', fontsize=20)

fig.tight_layout()
plt.show()
