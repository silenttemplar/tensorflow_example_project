import matplotlib.pyplot as plt
import numpy as np

n_student = 100
math_scores = np.random.normal(loc=50, scale=10, size=(n_student, ))

fig, ax = plt.subplots(figsize=(7, 7))

# example 1
# whis: IQR(InterQuartile Range)
# showfliers: 이상값 표현여부
'''
ax.boxplot(math_scores,
           notch=True, whis=1,
           showfliers=False)
'''

# example 2
medianprops = {'linewidth': 2, 'color': 'b'}
boxprops = {'linestyle': '-.', 'color': 'k', 'alpha': 0.7}
whiskerprops = {'linewidth': 2, 'color': 'tab:red', 'alpha': 0.8}

ax.boxplot(math_scores,
           notch=True,
           medianprops=medianprops, boxprops=boxprops,
           whiskerprops=whiskerprops, capprops=whiskerprops)

ax.grid(axis='y')

plt.show()

