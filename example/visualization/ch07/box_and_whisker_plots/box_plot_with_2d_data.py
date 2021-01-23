import matplotlib.pyplot as plt
import numpy as np

n_student = 100
kor_scores = np.random.normal(loc=50, scale=10, size=(n_student, 1))
math_scores = np.random.normal(loc=70, scale=10, size=(n_student, 1))
eng_scores = np.random.normal(loc=80, scale=10, size=(n_student, 1))
chem_scores = np.random.normal(loc=30, scale=10, size=(n_student, 1))

scores = np.hstack((kor_scores, math_scores, eng_scores, chem_scores))
labels = ['kor', 'math', 'eng', 'chem']
#print(scores.shape)

fig, ax = plt.subplots(figsize=(7, 7))

ax.boxplot(scores, labels=labels)
ax.set_ylim([0, 100])

major_yticks = np.arange(0, 101, 20)
minor_yticks = np.arange(0, 101, 5)

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)

ax.grid(axis='y',
        linewidth=2)
ax.grid(axis='y', which='minor',
        linewidth=2, linestyle=':')
ax.grid(axis='x', linewidth=0)

plt.show()

