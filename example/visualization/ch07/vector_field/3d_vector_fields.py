import matplotlib.pyplot as plt
import numpy as np

PI = np.pi

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
u = np.sin(PI*x) * np.cos(PI*y) * np.cos(PI*z)
v = -np.cos(PI*x) * np.sin(PI*y) * np.cos(PI*z)
w = np.sqrt(2.0/3.0) * np.cos(PI*x) * np.cos(PI*y) * np.sin(PI*z)


fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')

ax.quiver(x, y, z, u, v, w,
          length=0.1, normalize=True)

plt.show()

