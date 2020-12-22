import os

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from termcolor import colored

import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.optimizers import SGD

from tensorflow.keras.metrics import Mean
from tensorflow.keras.metrics import SparseCategoricalAccuracy

'''
[Tensorflow2 강의] 19강 Gradient Vanishing Problem 강의 예제샘플
https://www.youtube.com/watch?v=BM1S7AAXdRk&list=PLtm_YtKTtDkQJtgGSQnZzMJBRHyqANnQi&index=20
'''

def normalization(images, lables):
    images = tf.cast(images, tf.float32) / 255.
    return [images, lables]

train_ds, ds_info = tfds.load(name='mnist',
                             shuffle_files=True,
                             as_supervised=True,
                             split='train',
                             with_info=True)

n_layer = 7
#n_layer = 30
cmap = cm.get_cmap('rainbow', lut=n_layer+1)
units = [20]*n_layer

model = Sequential()
model.add(Flatten())
for layer_idx in range(n_layer - 1):
    model.add(Dense(units=units[layer_idx], activation='sigmoid'))
    #model.add(Dense(units=units[layer_idx], activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.build(input_shape=(None, 28, 28, 1))
model.summary()

train_batch_size = 10
train_ds = train_ds.map(normalization).batch(train_batch_size)

loss_object = SparseCategoricalCrossentropy()
optimizer = SGD()

train_ds_iter = iter(train_ds)
images, labels = next(train_ds_iter)

#print('images.shape: {}, labels.shape: {}'.format(images.shape, labels.shape))

with tf.GradientTape() as tape:
    predictions = model(images)
    loss = loss_object(labels, predictions)

gradients = tape.gradient(loss, model.trainable_variables)

# gradients 형태 및 길이 확인
#print('type(gradients): {}, len(gradients): {}'.format(type(gradients), len(gradients)))

# Gradient Vanishing 시각화
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_yscale('log')

# activation=sigmoid
for grad_idx, grad in enumerate(gradients[::2]):
    if grad_idx >= 1:
        grad_abs = np.abs(grad.numpy().flat)
        ax.plot(grad_abs, label='layer {}'.format(grad_idx),
                color=cmap(grad_idx), alpha=0.8)
ax.legend(bbox_to_anchor=(1,  0.5), loc='center left', fontsize=20)

# activation=relu
'''
grad_means = []
for grad_idx, grad in enumerate(gradients[::2]):
    if grad_idx >= 1:
        grad_abs = np.abs(grad.numpy().flat)
        grad_means.append(np.mean(grad_abs))
ax.plot(grad_means)
'''

fig.tight_layout()
plt.show()

