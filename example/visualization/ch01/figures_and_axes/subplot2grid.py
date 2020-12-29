import matplotlib.pyplot as plt

# 3x1
'''
ax1 = plt.subplot2grid((3,1), (0,0), colspan=2)
ax2 = plt.subplot2grid((3,1), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,1), (2,0), colspan=2)
'''

# 2x2
fig = plt.figure()
ax1 = plt.subplot2grid((2,2), (0,0), rowspan=2, fig=fig)
ax2 = plt.subplot2grid((2,2), (0,1), projection='3d', fig=fig)
ax3 = plt.subplot2grid((2,2), (1,1), projection='3d', fig=fig)

plt.show()