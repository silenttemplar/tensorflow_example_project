import matplotlib.pyplot as plt

xticks = [i for i in range(10)]
xticks_labels = ['Class ' + str(i) for i in xticks]
yticks = [i for i in range(0, 101, 20)]
yticks_labels = [str(i) +'%' for i in yticks]

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xticks(xticks)
ax.set_xticklabels(xticks_labels)

ax.set_yticks(yticks)
ax.set_yticklabels(yticks_labels)

ax.tick_params(axis='x',
                labelsize=15,
                rotation=60)
ax.tick_params(axis='y',
               labelsize=15)
fig.subplots_adjust(bottom=0.2, left=0.15)
#fig.tight_layout()

plt.show()