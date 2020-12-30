import matplotlib.pyplot as plt


fig, axes = plt.subplots(2, 2, figsize=(7, 7))

fig.suptitle('Title of Figure', fontsize=30, color='darkblue', alpha=0.9)
for ax_idx, ax in enumerate(axes.flat):
    ax.set_title('Ax {}'.format(ax_idx+1), fontsize=20)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')

plt.tight_layout()
#plt.subplots_adjust(bottom=0.05, top=0.8, hspace=0.3)
plt.show()
