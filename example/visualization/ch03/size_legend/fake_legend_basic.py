import matplotlib.pyplot as plt

c_arr = ['r', 'g', 'b']
s_arr = [500, 2000, 5000]

x_loc = [-2, 0, 2]
y_loc = x_loc

fig, ax = plt.subplots(figsize=(10, 10))
for plot_idx in range(len(c_arr)):
    '''
    ax.scatter(x_loc[plot_idx], y_loc[plot_idx],
               s=s_arr[plot_idx],
               c=c_arr[plot_idx],
               label='data'+str(plot_idx))
   '''
    # fake legend
    ax.scatter([], [],
               s=s_arr[plot_idx],
               c=c_arr[plot_idx],
               label='data'+str(plot_idx))

ax.legend(loc='center left',
          bbox_to_anchor=(1.05, 0.5),
          labelspacing=10,
          fontsize=20,
          edgecolor='None')

plt.tight_layout()
plt.show()