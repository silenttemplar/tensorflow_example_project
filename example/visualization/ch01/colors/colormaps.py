import matplotlib.pyplot as plt
import matplotlib.cm as cm

# example - color map
n_color = 10
cmap = cm.get_cmap('rainbow', lut=n_color)

#cmap = cm.get_cmap('tab10')
#n_color = len(cmap.colors)

fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, n_color])

for c_idx in range(n_color):
    color = cmap(c_idx)
    c_string_list = [c for c in str(color)]
    c_string = ''.join(c_string_list)

    ax.text(0, c_idx,
            'color='+c_string,
            fontsize=10,
            ha='center', color=color)

plt.show()