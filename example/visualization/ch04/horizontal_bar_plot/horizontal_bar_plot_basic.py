import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

data = np.arange(1, 6, 1)
data_idx = np.arange(len(data))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))

# vertical bar
axes[0].bar(data_idx, data)

# horizontal bar
axes[1].barh(data_idx, data)
axes[1].invert_yaxis()

plt.show()

