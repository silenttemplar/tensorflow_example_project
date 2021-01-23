import matplotlib.pyplot as plt
import numpy as np

n_student = 100
math_scores = np.random.normal(loc=50, scale=10, size=(n_student, ))

fig, ax = plt.subplots(figsize=(7, 7))
ax.boxplot(math_scores)

plt.show()

