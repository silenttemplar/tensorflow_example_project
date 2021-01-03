import matplotlib.pyplot as plt

# example 1
'''
fig, ax = plt.subplots(figsize=(10, 10))
xaxis = ax.get_xaxis()
yaxis = ax.get_yaxis()

xaxis.set_visible(False)
yaxis.set_visible(False)
'''

# example 2
fig, axes = plt.subplots(3, 3, figsize=(10, 10))

# positioning
#fig.subplots_adjust(bottom=0.01, top=0.99, left=0.01, right=0.99)

# spacing
#fig.subplots_adjust(hspace=0.2, wspace=0.05)

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()
