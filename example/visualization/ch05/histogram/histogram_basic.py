import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 500
data = np.random.normal(0, 5, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 7))
freqs, bin_edges, rects = ax.hist(data,
                                  facecolor='skyblue', edgecolor='darkblue',
                                  hatch='//')
# 통계적 정보 표현
n_bin = len(freqs)
bin_edges_around = np.around(bin_edges, 2)

m_val, M_val = bin_edges_around[0], bin_edges_around[-1]
bin_interval = np.around(bin_edges[1]-bin_edges[0], 2)

text_loc = ax.get_xlim()[0], ax.get_ylim()[1]
text_template = 'Number of Bins: {}\n' + 'Min, Max Values: {} / {}\n' + 'Bin Interval: {}'
ax.text(text_loc[0]+0.1, text_loc[1]-10, text_template.format(n_bin, m_val, M_val, bin_interval))

# 주어진 edges 으로 center 계산
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2

ax.set_xticks(bin_centers)
ax.set_xticklabels(np.round(bin_centers, 2), rotation=30)

for rect in rects:
    x = rect.get_x()
    width = rect.get_width()
    height = rect.get_height()
    ax.text(x + width/2, height+2, str(height), ha='center')

plt.show()
