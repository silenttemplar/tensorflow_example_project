import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data1, n_data2 = 300, 300
data1 = np.random.normal(0, 1, (n_data1,))
data2 = np.random.normal(5, 3, (n_data2,))

data = np.stack((data1, data2))
m_val, M_val = data.min(), data.max()
bin_loc = np.linspace(m_val, M_val, 31)
bin_center = (bin_loc[:-1] + bin_loc[1:]) / 2
xticks = bin_center[::2]

fig, ax = plt.subplots(figsize=(14, 10))
ax.tick_params(labelsize=20)

ax.hist(data1, bins=bin_loc, alpha=0.5)
ax.hist(data2, bins=bin_loc, alpha=0.5)

ax.set_xticks(xticks)
ax.set_xticklabels(np.around(xticks, 2), rotation=30)
ax.set_xticks(bin_center, minor=True)
ax.grid()
ax.grid(which='minor', linestyle=':')

plt.show()

