import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

np.random.seed(0)

n_can = 5
cans = np.array(['A', 'B', 'C', 'D', 'E'])

votes = np.random.randint(100, 1000, (2, n_can))
votes_sum = np.sum(votes, axis=0)

total_votes = np.sum(votes_sum)
percentages = votes_sum/total_votes * 100
percentages_tmp = votes/total_votes * 100

textprops = {'fontsize': 30, 'color': 'w'}
wedgeprops = {'width':0.4, 'edgecolor':'lightsteelblue', 'linewidth':2}

cmap = cm.get_cmap('tab20c', lut=20)
outer_colors = [cmap(4*i) for i in range(n_can)]
inner_colors = [cmap(4*i + j+1) for i in range(n_can) for j in range(2)]



fig, ax = plt.subplots(figsize=(10, 10), facecolor='lightsteelblue')

wedges, texts, autotexts = ax.pie(percentages,
                                  autopct='%1.1f%%',
                                  pctdistance=0.8,
                                  textprops=textprops, wedgeprops=wedgeprops,
                                  colors=outer_colors)
ax.pie(percentages_tmp.flatten(order='F'),
       colors=inner_colors,
       wedgeprops=wedgeprops,
       radius=0.55)

fig.tight_layout()
plt.show()

