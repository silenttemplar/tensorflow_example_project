import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

plt.style.use('seaborn')

X, Y, Z = get_test_data(0.05)
levels = np.linspace(Z.min(), Z.max(), 30)

fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# wireframe
ax1.plot_wireframe(X, Y, Z)
ax1.contour(X, Y, Z, cmap='hot', levels=levels, offset=Z.min()-5)

# contour
ax2.contour(X, Y, Z, cmap='hot', levels=levels)

plt.show()