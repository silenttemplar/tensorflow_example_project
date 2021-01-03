import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))

# example 1
'''
for spine_loc, spine in ax.spines.items():
    if spine_loc in ('right', 'top'):
        spine.set_visible(False)
'''

# example 2
for spine_loc, spine in ax.spines.items():
    if spine_loc in ('left', 'bottom'):
        spine.set_visible(False)

ax.tick_params(left=False, labelleft=False,
               right=True, labelright=True,
               bottom=False, labelbottom=False,
               top=True, labeltop=True)


plt.show()