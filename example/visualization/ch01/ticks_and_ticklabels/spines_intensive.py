import matplotlib.pyplot as plt
import numpy as np

noise_data = np.random.normal(0, 1, (100, ))

fig, ax = plt.subplots(figsize=(7 ,7))

# example0
'''
for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right','top']:
        spine.set_visible(False)

    if spine_loc in ['left','bottom']:
        spine.set_position('center')
'''

# example1
ax.plot(noise_data)
ax.tick_params(labelsize=15)

for spine_loc, spine in ax.spines.items():
    if spine_loc in ['right','top']:
        spine.set_visible(False)

    '''
    if spine_loc in ['bottom']:
        #spine.set_position('center')
        spine.set_position(('axes', 0.5))
    '''

    if spine_loc in ['bottom','left']:
        spine.set_position(('data', 0))

    if spine_loc in ['left','bottom']:
        spine.set_color('navy')
        spine.set_linewidth(2)

fig.tight_layout()

plt.show()

