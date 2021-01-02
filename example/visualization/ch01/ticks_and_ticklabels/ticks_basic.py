import matplotlib.pyplot as plt

major_xticks = [i for i in range(0, 11, 2)]
minor_xticks = [i for i in range(0, 11, 1)]

fig, ax = plt.subplots()

ax.tick_params(labelsize=15,
               length=10,
               width=3,
               rotation=30,
               top=True, labeltop=True)

# set major, minor xticks
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)

plt.show()

