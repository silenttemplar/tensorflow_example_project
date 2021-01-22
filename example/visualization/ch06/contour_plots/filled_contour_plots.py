import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

plt.style.use('seaborn')

# example1
'''
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
levels = np.geomspace(Z.min(), Z.max(), 100)
'''

# example2
X, Y, Z = get_test_data(0.05)
levels = np.linspace(Z.min(), Z.max(), 100)

fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# wireframe
ax1.plot_wireframe(X, Y, Z)

# contour/contourf
#ax2.contour(X, Y, Z, cmap='bwr', levels=levels)
contourf = ax2.contourf(X, Y, Z, cmap='bwr', levels=levels)
cbar = fig.colorbar(contourf, pad=0., fraction=0.15)

contourf_zero = ax2.contour(X, Y, Z, cmap='Greys', levels=0, linestyles=':', linewidths=5)
ax2.clabel(contourf_zero, [0], fontsize=20)

fig.tight_layout()
plt.show()
