import matplotlib.pyplot as plt
import numpy as np

# example1
'''
n_data = 100

random_noise1 = np.random.normal(0, 1, (n_data,))
random_noise2 = np.random.normal(1, 1, (n_data,))
random_noise3 = np.random.normal(2, 1, (n_data,))

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(random_noise1)
ax.plot(random_noise2)
ax.plot(random_noise3)
'''

# example2
n_data1, n_data2, n_data3 = 200, 50, 10

x_data1 = np.linspace(0, 200, n_data1)
x_data2 = np.linspace(0, 200, n_data2)
x_data3 = np.linspace(0, 200, n_data3)

random_noise1 = np.random.normal(0, 1, (n_data1,))
random_noise2 = np.random.normal(1, 1, (n_data2,))
random_noise3 = np.random.normal(2, 1, (n_data3,))

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(x_data1, random_noise1)
ax.plot(x_data2, random_noise2)
ax.plot(x_data3, random_noise3)

# example3
'''
PI = np.pi
t = np.linspace(-4*PI, 4*PI, 1000).reshape(1, -1)
sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)
data = np.vstack((sin, cos, tan))
#print(data)

title_list = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']
x_ticks = np.arange(-4*PI, 4*PI+PI, PI)
x_ticklabels = [str(i) + r'$\pi$' for i in range(-4, 5)]

fig, axes = plt.subplots(3, 1, sharex=True)

for ax_idx, ax in enumerate(axes.flat):
    ax.plot(t.flatten(), data[ax_idx])
    ax.set_title(title_list[ax_idx])
    ax.grid()
    if ax_idx == 2:
        ax.set_ylim([-3, 3])

axes[-1].set_xticks(x_ticks)
axes[-1].set_xticklabels(x_ticklabels)
'''

plt.show()
