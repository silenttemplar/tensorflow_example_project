import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 500
data = np.random.normal(0, 5, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 7))

# bins: 나뉘는 구간 수 지정
ax.hist(data,
        facecolor='skyblue', edgecolor='darkblue',
        linewidth=3)
ax.hist(data,
        bins=20,
        facecolor='coral', edgecolor='red',
        linewidth=3)

# density: 전체 수 100% 일때, 구간 합이 1이 되도록 변경
'''
freqs, bin_edges, rects = ax.hist(data, density=True)

bin_interval = bin_edges[1] - bin_edges[0]
print(freqs*bin_interval)
print(np.sum(freqs*bin_interval))
'''

# cumulative: 누적분포도
'''
ax.hist(data, cumulative=True)
'''

#orientation: vertical (default) / horizontal 표현여부 지정
'''
ax.hist(data, orientation='horizontal')
'''

# rwith: 막대너비 (초기값=1)
'''
ax.hist(data, rwidth=0.8)
'''

# align: 막대정렬
'''
ax.hist(data,
        rwidth=0.4, align='right',
        facecolor='skyblue', edgecolor='darkblue',
        linewidth=3)
plt.grid()
'''

plt.show()