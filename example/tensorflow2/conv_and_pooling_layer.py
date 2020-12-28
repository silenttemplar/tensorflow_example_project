import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D


'''
[Tensorflow2 강의] 21강 Conv and Pooling Layer 강의 예제샘플
'''

conv = Conv2D(filters=8, kernel_size=3, padding='valid', activation='relu')
pool = MaxPooling2D(pool_size=2, strides=2)

#image = tf.random.normal(mean=0, stddev=1, shape=(1, 28, 28, 1))
image = tf.random.normal(mean=0, stddev=1, shape=(1, 28, 28, 3))
conved = conv(image)
pooled = pool(conved)

print('image.shape: {}, conved.shape: {}, pooled.shape: {}'.format(image.shape, conved.shape, pooled.shape))
print('conv.weight.shape: {}, conv.bias.shape:{}'.format(conv.get_weights()[0].shape, conv.get_weights()[1].shape))
