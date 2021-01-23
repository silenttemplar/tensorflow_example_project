import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(0, 4*PI, 40)
cos = np.cos(t)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(14, 7))

ax.stem(cos,
        label='cos',
        use_line_collection=True,
        linefmt='r:', markerfmt='ro',
        basefmt='k')
ax.stem(sin,
        label='sin',
        use_line_collection=True,
        linefmt='b:', markerfmt='bo',
        basefmt='k')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

major_yticks = np.arange(-1, 1+0.01, 0.5)
minor_yticks = np.arange(-1, 1+0.01, 0.25)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.grid(axis='y')
ax.grid(axis='y', which='minor',
        linewidth=2, linestyle=':')
ax.legend(loc='upper center',
          bbox_to_anchor=(0.5, 0), ncol=2, fontsize=20)

fig.tight_layout()
plt.show()