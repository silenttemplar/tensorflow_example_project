import matplotlib.pyplot as plt
import numpy as np

# example1
'''
x_data = np.array([0, 1])
y_data = x_data

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(x_data, y_data)
ax.plot(x_data, y_data+1, linestyle=':')
ax.plot(x_data, y_data+2, linestyle='--')
ax.plot(x_data, y_data+3, linestyle='-.')
'''

# example2
PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin)
ax.axhline(y=1, linestyle=':', color='r')
ax.axhline(y=-1, linestyle=':', color='b')

plt.show()