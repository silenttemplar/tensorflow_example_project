import matplotlib.pyplot as plt


fig = plt.figure(figsize=(7, 7), facecolor='linen')

# 1x1
'''
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
'''

# example.1
'''
left, bottom = 0.1, 0.1
spacing = 0.05
width1, height1 = 0.5, 0.5

width2 = 1 - (2*left + width1 + spacing)
height2 = 1 - (2*bottom + height1 + spacing)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, 1 - 2*left, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)
'''

# example.2
'''
left, bottom = 0.1, 0.1
spacing = 0.005
width1, height1 = 0.65, 0.65

width2 = 1 - (2*left + width1 + spacing)
height2 = 1 - (2*bottom + height1 + spacing)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, width1, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)
'''

# example.3 - zoom axes
ax = fig.add_subplot(111)
ax_zoom = fig.add_axes([0.4, 0.4, 0.45, 0.45])

plt.show()