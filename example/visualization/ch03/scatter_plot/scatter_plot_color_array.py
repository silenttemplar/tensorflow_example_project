import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

PI = np.pi
n_point = 100

t = np.linspace(-4*PI, 4*PI, n_point)
sin = np.sin(t)

# color array
cmap = cm.get_cmap('Reds', lut=n_point)
c_arr = [cmap(c_idx) for c_idx in range(n_point)]

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(t, sin, s=300, c=c_arr)

plt.show()