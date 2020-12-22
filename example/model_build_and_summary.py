import os
import json
import numpy as os
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Flatten, Dense, Activation
from tensorflow.keras.layers import InputLayer

# cnn
from tensorflow.keras.layers import  Conv2D, MaxPool2D, Dropout

'''
[Tensorflow2 강의] 17강 Model Build and Summary 강의 예제샘플
https://www.youtube.com/watch?v=KdSoVNUr82k&list=PLtm_YtKTtDkQJtgGSQnZzMJBRHyqANnQi&index=18
'''

def get_test_model():
    model = Sequential()
    #model.add(InputLayer(input_shape=(28, 28, 1)))
    model.add(Flatten())
    model.add(Dense(units=10))
    model.add(Activation('relu'))
    model.add(Dense(units=2))
    model.add(Activation('softmax'))
    return model

def get_test_model2():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(units=10))
    model.add(Activation('relu'))
    model.add(Dense(units=2))
    model.add(Activation('softmax'))

    print(model.built)
    test_img = tf.random.normal(shape=(1, 28, 28, 1))
    model(test_img)
    print(model.built)

    return model

def get_cnn_model():
    model = Sequential()
    model.add(Conv2D(filters=10, kernel_size=(3, 3), padding='valid',
                     name='conv_1'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2,
                        name='conv_1_maxpool'))
    model.add(Activation('relu', name='conv_1_act'))
    model.add(Conv2D(filters=10, kernel_size=(3, 3), padding='valid',
                     name='conv_2'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2,
                        name='conv_2_maxpool'))
    model.add(Activation('relu', name='conv_2_act'))
    model.add(Flatten())
    model.add(Dense(units=32, activation='relu', name='dense_1'))
    model.add(Dense(units=10, activation='softmax', name='dense_2'))

    return model

class TestModel(Model):
    def __init__(self):
        super(TestModel, self).__init__()

        self.flatten = Flatten()
        self.d1 = Dense(units=10, name='dense_1')
        self.d1_act = Activation('relu', name='dense_1_act')
        self.d2 = Dense(units=2, name='dense_2')
        self.d2_act = Activation('softmax', name='softmax')

    def call(self, x):
        x = self.flatten(x)
        x = self.d1(x)
        x = self.d1_act(x)
        x = self.d2(x)
        output = self.d2_act(x)
        return output

if __name__ == '__main__':
    #model = get_test_model()
    model = TestModel()
    #model = get_test_model2()
    #model = get_cnn_model()

    # batch_size / height, weight  / channel
    model.build(input_shape=(None, 28, 28, 1))
    model.summary()

    #tf.keras.backend.clear_session()

