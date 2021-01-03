import matplotlib.pyplot as plt

major_xticks = [i for i in range(0, 11, 2)]
minor_xticks = [i for i in range(0, 11, 1)]

fig, ax = plt.subplots(figsize=(7, 7))

# set major, minor xticks
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)

ax.grid(axis='x',
        which='major', linewidth=1.5)
ax.grid(axis='x',
        which='minor', linestyle=':')

plt.show()