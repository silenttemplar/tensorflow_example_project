import tensorflow as tf
from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Layer, Conv2D, AveragePooling2D
from tensorflow.keras.layers import Flatten, Dense, ZeroPadding2D


'''
[Tensorflow2 강의] 23강 LeNet Impl with Sub classing 강의 예제샘플
'''

class FeatureExtrator(Layer):
    def __init__(self, filter1, tilter2):
        super(FeatureExtrator, self).__init__()

        self.conv1 = Conv2D(filters=filter1, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv1_pool = AveragePooling2D(pool_size=2, strides=2)
        self.conv2 = Conv2D(filters=tilter2, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv2_pool = AveragePooling2D(pool_size=2, strides=2)

    def call(self, x):
        x = self.conv1(x)
        x = self.conv1_pool(x)
        x = self.conv2(x)
        x = self.conv2_pool(x)

        return x

class LeNet1(Model):
    def __init__(self):
        super(LeNet1, self).__init__()

        # feature extractor
        self.fe = FeatureExtrator(4, 12)

        '''
        self.fe = Sequential()
        self.fe.add(Conv2D(filters=4, kernel_size=5, padding='valid', strides=1, activation='tanh'))
        self.fe.add(AveragePooling2D(pool_size=2, strides=2))
        self.fe.add(Conv2D(filters=12, kernel_size=5, padding='valid', strides=1, activation='tanh'))
        self.fe.add(AveragePooling2D(pool_size=2, strides=2))
        '''

        '''
        self.conv1 = Conv2D(filters=4, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv1_pool = AveragePooling2D(pool_size=2, strides=2)
        self.conv2 = Conv2D(filters=12, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv2_pool = AveragePooling2D(pool_size=2, strides=2)
        '''

        # classifier
        self.classifier = Sequential()
        self.classifier.add(Flatten())
        self.classifier.add(Dense(units=10, activation='softmax'))

        '''
        self.flatten = Flatten()
        self.d1 = Dense(units=10, activation='softmax')
        '''

    def call(self, x):
        x = self.fe(x)
        x = self.classifier(x)

        '''
        x = self.conv1(x)
        x = self.conv1_pool(x)
        x = self.conv2(x)
        x = self.conv2_pool(x)
        x = self.flatten(x)
        x = self.d1(x)
        '''

        return x

class LeNet4(Model):
    def __init__(self):
        super(LeNet4, self).__init__()

        # feature extractor
        self.fe = FeatureExtrator(4, 16)
        '''
        self.conv1 = Conv2D(filters=4, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv1_pool = AveragePooling2D(pool_size=2, strides=2)
        self.conv2 = Conv2D(filters=16, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv2_pool = AveragePooling2D(pool_size=2, strides=2)
        '''

        # classifier
        self.flatten = Flatten()
        self.d1 = Dense(units=120, activation='tanh')
        self.d2 = Dense(units=10, activation='softmax')

    def call(self, x):
        x = self.fe(x)
        '''
        x = self.conv1(x)
        x = self.conv1_pool(x)
        x = self.conv2(x)
        x = self.conv2_pool(x)
        x = self.flatten(x)
        '''

        x = self.flatten(x)
        x = self.d1(x)
        x = self.d2(x)
        return x

class LeNet5(Model):
    def __init__(self, activation):
        super(LeNet5, self).__init__()

        # feature extractor
        self.fe = FeatureExtrator(6, 16)
        '''
        self.conv1 = Conv2D(filters=6, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv1_pool = AveragePooling2D(pool_size=2, strides=2)
        self.conv2 = Conv2D(filters=16, kernel_size=5, padding='valid', strides=1, activation='tanh')
        self.conv2_pool = AveragePooling2D(pool_size=2, strides=2)
        '''

        # classifier
        self.flatten = Flatten()
        self.d1 = Dense(units=140, activation='tanh')
        self.d2 = Dense(units=84, activation='tanh')
        self.d3 = Dense(units=10, activation='softmax')

    def call(self, x):
        x = self.fe(x)
        '''
        x = self.conv1(x)
        x = self.conv1_pool(x)
        x = self.conv2(x)
        x = self.conv2_pool(x)
        '''

        x = self.flatten(x)
        x = self.d1(x)
        x = self.d2(x)
        x = self.d3(x)

        return x

if __name__ == '__main__':
    pass