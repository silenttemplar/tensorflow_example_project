import matplotlib.pyplot as plt


# example 1
'''
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_title('title')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
'''

# example 2
title_list = ['Ax' + str(i) for i in range(4)]
xlabel_list = ['x label' + str(i) for i in range(4)]
ylabel_list = ['y label' + str(i) for i in range(4)]

print('title_list: {}'.format(title_list))
print('xlabel_list: {}'.format(xlabel_list))
print('ylabel_list: {}'.format(ylabel_list))

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx])
    ax.set_xlabel(xlabel_list[ax_idx])
    ax.set_ylabel(ylabel_list[ax_idx])

fig.tight_layout()
plt.show()
