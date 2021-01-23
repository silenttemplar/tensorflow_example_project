import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)

X, Y = np.meshgrid(x, y)
X_t = tf.Variable(X)
Y_t = tf.Variable(Y)

with tf.GradientTape() as tape:
    Z_t = X_t**2 + Y_t**2

gradients = tape.gradient(Z_t, [X_t, Y_t])
#print(gradients)

Z = Z_t.numpy()
dX = gradients[0].numpy()
dY = gradients[1].numpy()

levels = np.geomspace(np.min(Z), np.max(Z), 30)

fig, ax = plt.subplots(figsize=(10, 10))
ax.contour(X, Y, Z,
           levels=levels,
           cmap='hot', alpha=0.5)

# (X, Y): point, (dX, dY): Vector
ax.quiver(X, Y, dX, dY)

plt.show()


