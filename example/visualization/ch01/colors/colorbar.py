import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# example - color bar
x = np.linspace(-10, 10, 100)
y = x

X, Y = np.meshgrid(x, y)
Z = np.power(X, 2) + np.power(Y, 2)

levels = np.linspace(np.min(Z), np.max(Z), 30)
cmap = cm.get_cmap('Reds_r', lut=len(levels))

fig, ax = plt.subplots(figsize=(8, 7))
cf = ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
cbar = fig.colorbar(cf, ax=ax)

plt.show()
