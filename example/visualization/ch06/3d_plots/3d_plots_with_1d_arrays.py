import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn')

# data
PI = np.pi
n_point = 300

t = np.linspace(0, 10*PI, n_point)
x = t*np.cos(t)
y = t*np.sin(t)
z = 0.2*t

# noise data
noise_coeff = 0.1
x_noise = x + noise_coeff*np.random.normal(0, 1, n_point)
y_noise = y + noise_coeff*np.random.normal(0, 1, n_point)
z_noise = z + noise_coeff*np.random.normal(0, 1, n_point)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')

ax.plot(x, y, z,
        alpha=0.7, color='r', linewidth=3, linestyle='-.')

# project to x-y dimension
zlim = ax.get_zlim()
ax.plot(x, y, zlim[0]*np.ones(n_point), color='gray')

# scatter
ax.scatter(x_noise, y_noise, z_noise, s=100)

# text
ax.text(0.5, 0.5, 0.5, 'hello world',
        fontsize=30,
        ha='center', va='center',
        zdir=(0, 0, 1))

ax.set_xlabel('X Axis', fontsize=20, labelpad=20)
ax.set_ylabel('Y Axis', fontsize=20, labelpad=20)
ax.set_zlabel('Z Axis', fontsize=20, labelpad=20)


fig.subplots_adjust(top=1, bottom=0, left=0, right=1)

plt.show()
