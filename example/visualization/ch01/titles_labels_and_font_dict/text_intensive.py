import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

'''
- fontweight
- alpha
- color
'''
ax.text(x=0, y=0, s='(0, 0)')
ax.text(x=0.5, y=0.5, s='(0.5, 0.5)', fontweight='bold')
ax.text(x=0.5, y=-0.5, s='(0.5, -0.5)', fontweight='bold', alpha=0.3, color='red')
ax.text(x=-0.5, y=0.5, s='(-0.5, 0.5)')
ax.text(x=-0.5, y=-0.5, s='(-0.5, -0.5)', alpha=0.3, color='red')

'''
- font dict
'''
title_font_dict = {'fontsize': 20, 'color': 'darkblue'}
ax.set_title('Title', fontdict=title_font_dict)

plt.show()