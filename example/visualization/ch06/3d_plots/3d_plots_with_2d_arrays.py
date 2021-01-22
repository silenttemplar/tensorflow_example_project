import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

plt.style.use('seaborn')

x = np.arange(-5, 5, 0.25)
y =np.arange(-5, 5, 0.25)
#print(x.shape, y.shape)
#print(x, y)


X, Y = np.meshgrid(x, y)

coordinates = np.empty(X.shape, dtype=object)
for r_idx in range(X.shape[0]):
    for c_idx in range(X.shape[1]):
        coordinates[r_idx, c_idx] = (X[r_idx, c_idx], Y[r_idx, c_idx])
#print(coordinates)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
#print('X:\n', X)
#print('Y:\n', Y)
#print('R:\n', R)
#print('Z:\n', Z)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# wireframe
ax.plot_wireframe(X, Y, Z, ccount=10, rcount=5)
#ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5)

# surface
'''
surface = ax.plot_surface(X, Y, Z, cmap='hot')
cbar = fig.colorbar(surface,
                    orientation='horizontal',
                    fraction=0.1, pad=0., shrink=0.9)
cbar_ticks = np.arange(-1, 1, 0.25)
cbar.set_ticks(cbar_ticks)
cbar.ax.set_xticklabels(cbar_ticks, fontsize=20)
'''

# normaled surface
'''
norm = plt.Normalize(Z.min(), Z.max())
Z_normaled = norm(Z)
facecolors = cm.jet(Z_normaled)

surface = ax.plot_surface(X, Y, Z, facecolors=facecolors)
surface.set_facecolor((0, 0, 0, 0))
'''

ax.set_xlabel('X Axis', fontsize=20, labelpad=20)
ax.set_ylabel('Y Axis', fontsize=20, labelpad=20)
ax.set_zlabel('Z Axis', fontsize=20, labelpad=20)
ax.tick_params(labelsize=10)


fig.subplots_adjust(bottom=0, top=1, left=0, right=1)

plt.show()

