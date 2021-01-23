import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

np.random.seed(0)

n_can = 5
cans = np.array(['A', 'B', 'C', 'D', 'E'])

votes = np.random.randint(100, 1000, (n_can,))
total_votes = np.sum(votes)
percentages = votes/total_votes * 100

sort_idx = np.argsort(percentages)
percentages_sort = percentages[sort_idx]
cans_sort = cans[sort_idx]

fig, ax = plt.subplots(figsize=(10, 10), facecolor='lightsteelblue')

textprops = {'fontsize': 30, 'color': 'w'}
wedgeprops = {'edgecolor':'lightsteelblue', 'linewidth': 5}

cmap = cm.get_cmap('tab10')
colors = [cmap(i) for i in range(n_can)]

explode = [0, 0, 0, 0, 0.1]

wedges, texts, autotexts = ax.pie(percentages_sort,
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  textprops=textprops, wedgeprops=wedgeprops,
                                  colors=colors,
                                  explode=explode)

ax.legend(wedges[::-1], cans_sort[::-1],
          title='Candidate',
          title_fontsize=20, fontsize=20,
          loc='center left',
          bbox_to_anchor=(0.9, 0.5))

fig.tight_layout()
plt.show()

