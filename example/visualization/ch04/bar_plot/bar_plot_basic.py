import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 10
data = np.random.uniform(10, 100, (n_data, ))

data_idx = np.arange(n_data)
data_labels = np.array(['class '+str(i) for i in range(n_data)])

# sorted data, label
sort_idx = np.argsort(data)
data_sort = data[sort_idx]
data_labels_sort = data_labels[sort_idx]

major_yticks = np.arange(0, 101, 20)
major_yticklabels = [str(p)+'%' for p in major_yticks]
minor_yticks = np.arange(0, 101, 5)

fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=15)

# common bar
ax.bar(data_idx, data)
ax.set_xticks(data_idx)
ax.set_xticklabels(data_labels, rotation=-30, ha='left')

# sorted bar
'''
ax.bar(data_idx, data_sort)
ax.set_xticks(data_idx)
ax.set_xticklabels(data_labels_sort, rotation=-30, ha='left')
'''

ax.set_yticks(major_yticks)
ax.set_yticklabels(major_yticklabels)
ax.set_yticks(minor_yticks, minor=True)

ax.grid(axis='y')

plt.show()
