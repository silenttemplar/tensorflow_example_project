import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(0.01, 5*PI, 100)
sin = np.sin(t)
exp = np.exp(t)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot()
ax1.plot(t, sin, color='orange')
ax1.set_ylabel('sin')

# y축 공유토록 지정
ax2 = ax1.twinx()

# 지정한 scale로 변환표현
#ax2.set_yscale('log')

ax2.plot(t, exp, color='blue')
ax2.set_ylabel('exp')

plt.show()