import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(0, 4*PI, 40)
cos = np.cos(t)
sin = np.sin(t)

fig, axes = plt.subplots(2, 2, figsize=(20, 10))
axes[0, 0].plot(cos)
axes[0, 1].stem(cos, use_line_collection=True)
axes[1, 0].plot(sin)
axes[1, 1].stem(sin, use_line_collection=True)

fig.tight_layout()
plt.show()