import matplotlib.pyplot as plt

from example.visualization.ch02.dataset.bop_utils import *

np.random.seed(0)

# example2
dataset = bop_data_reader()
t_year = 90
t_year_data = get_year_data(dataset, t_year)

# x labels 생성
month_dict = {m:None for m in range(1, 1+12)}
for data_idx, data in enumerate(t_year_data):
    Y, M, D, price = data
    if month_dict[M] is None:
        month_dict[M] = [data_idx, '-'.join(str(int(i)) for i in [Y, M, D])]
first_day_label = np.array(list(month_dict.values()))
x_arange  = np.arange(t_year_data.shape[0])
#print(first_day_label)

# 시각화
fig, ax = plt.subplots(figsize=(15, 10))

ax.plot(x_arange, t_year_data[:,-1])

ax.set_xticks(first_day_label[:,0].astype(np.int))
ax.set_xticklabels(first_day_label[:,1], rotation=-30, ha='left')

ax.set_title("BOP data({})".format(t_year), fontsize=30)
ax.set_ylabel('daily prices in USD', fontsize=25)
ax.tick_params(labelsize=20)
ax.grid()

# example1
'''
y_data = np.random.normal(loc=0, scale=1, size=(300,))
#print(y_data)

fig, ax = plt.subplots(figsize=(7, 7))
ax.plot(y_data)

fig.tight_layout(pad=3)
ax.tick_params(labelsize=15)

major_xticks = np.arange(301, step=100)
#minor_xticks = np.arange(301, step=50)
ax.set_xticks(major_xticks)
#ax.set_xticks(minor_xticks, minor=True)

ax.grid()
for spine_loc, spine in ax.spines.items():
    spine.set_linewidth(3)

    if spine_loc in ['right', 'top']:
        spine.set_visible(False)
    if spine_loc in ['bottom', 'left']:
        spine.set_position(('data', 0))
'''

# example3
'''
n_data = 100
s_idx= 30
x_data = np.arange(s_idx, s_idx+n_data)
y_data = np.random.normal(0, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.tight_layout(pad=3)
x_ticks = np.arange(s_idx, s_idx+n_data+1, 20)
ax.set_xticks(x_ticks)
ax.grid()
'''

plt.show()