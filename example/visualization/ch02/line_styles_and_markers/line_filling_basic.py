import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 20)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(t, sin, label='sin(t)', color='black')
ax.axhline(y=0, color='black')

ax.fill_between(t, sin,
                alpha=0.3,
                hatch='/',
                edgecolor='b',
                where=sin>=0,
                interpolate=True)

ax.fill_between(t, sin,
                alpha=0.3,
                hatch='/',
                edgecolor='r',
                where=sin<0,
                interpolate=True)

plt.show()