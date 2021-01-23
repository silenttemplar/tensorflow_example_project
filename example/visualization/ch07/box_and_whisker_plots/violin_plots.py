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

fig, axes = plt.subplots(1, 2,  figsize=(14, 7))

# violin plot
axes[0].violinplot(scores)

# box plot
axes[1].boxplot(scores)


axes[0].set_ylim([0, 100])
axes[1].set_ylim([0, 100])

plt.show()

