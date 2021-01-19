import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data1, n_data2 = 300, 300
data1 = np.random.normal(0, 1, (n_data1,))
data2 = np.random.normal(5, 3, (n_data2,))

fig, ax = plt.subplots(figsize=(14, 10))
ax.tick_params(labelsize=20)

ax.hist(data1, bins=30, alpha=0.5)
ax.hist(data2, bins=30, alpha=0.5)
plt.show()

