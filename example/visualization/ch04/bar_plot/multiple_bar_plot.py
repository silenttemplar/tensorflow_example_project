import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_class = 2
width = 0.8
bar_width = width / n_class

n_data = 10
data = np.random.uniform(10, 100, (n_data, ))
data2 = np.random.uniform(10, 100, (n_data, ))
data3 = np.random.uniform(10, 100, (n_data, ))
data_idx = np.arange(n_data)

xticks = np.arange(-1, 10, 0.5)

major_yticks = np.arange(0, 101, 20)
major_yticklabels = [str(p)+'%' for p in major_yticks]
minor_yticks = np.arange(0, 101, 5)

fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=15)

# example1 - basic
'''
ax.bar(data_idx, data,
       width=0.4,
       align='edge')
ax.bar(data_idx, data2,
       width=-0.4,
       align='edge')
'''

# example2 - 2개
ax.bar(data_idx - bar_width/2, data,
       width=bar_width,
       label='data')
ax.bar(data_idx + bar_width/2, data3,
       width=bar_width,
       label='data1')

# example3 - 3개
'''
ax.bar(data_idx - bar_width/2*2, data,
       width=bar_width,
       label='data')
ax.bar(data_idx, data2,
       width=bar_width,
       label='data2')
ax.bar(data_idx + bar_width/2*2, data3,
       width=bar_width,
       label='data3')
'''

ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=30)
ax.set_yticks(major_yticks)
ax.set_yticklabels(major_yticklabels)
ax.set_yticks(minor_yticks, minor=True)

ax.grid(axis='y')
plt.legend()


plt.show()
