import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

ax.text(x=0, y=0, s='(0, 0)')
ax.text(x=0.5, y=0.5, s='(0.5, 0.5)', va='top', ha='right')
ax.text(x=0.5, y=-0.5, s='(0.5, -0.5)', va='bottom', ha='right')
ax.text(x=-0.5, y=0.5, s='(-0.5, 0.5)', va='top', ha='left')
ax.text(x=-0.5, y=-0.5, s='(-0.5, -0.5)', va='bottom', ha='left')
ax.grid()

plt.show()