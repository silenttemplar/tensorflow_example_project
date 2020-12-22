import json
import numpy as np
from termcolor import colored

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Activation
from tensorflow.keras.layers import  Conv2D, MaxPool2D, Dropout

'''
[Tensorflow2 강의] 18강 Model Configuration and Params 강의 예제샘플
https://www.youtube.com/watch?v=hT0oBjtjp8Y&list=PLtm_YtKTtDkQJtgGSQnZzMJBRHyqANnQi&index=19
'''

model = Sequential()

# feature extractor
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

# classifier
model.add(Flatten())
model.add(Dense(units=32, name='dense_1'))
model.add(Activation('relu', name='dense_1_act'))
model.add(Dense(units=10, name='dense_2'))
model.add(Activation('softmax', name='dense_2_act'))

# build
model.build(input_shape=(None, 28, 28, 1))
#model.summary()

#print(colored('model.layers', 'cyan'), '\n', model.layers)
#print(colored('len(model.layers)', 'cyan'), '\n', len(model.layers))

# layer 내 config 확인 (1)
'''
final_layer = model.layers[-1]
final_layer_config = final_layer.get_config()
print(json.dumps(final_layer_config, indent=2))

print(colored('type(final_layer_config)', 'cyan'), '\n',
      type(final_layer_config))
print(colored('final_layer_config.keys()', 'cyan'), '\n',
      final_layer_config.keys())
print(colored('final_layer_config.values()', 'cyan'), '\n',
      final_layer_config.values())
'''

# layer 내 config 확인 (2) - layer 목록 내 원하는 정보 추출
'''
for layer in model.layers:
    layer_config = layer.get_config()
    #print(json.dumps(layer_config, indent=2))

    layer_name = layer_config['name']
    if layer_name.startswith('conv') and len(layer_name.split('_')) <=2:
        print(colored('layer_name: ', 'cyan'), layer_name)
        print('n filters: ', layer_config['filters'])
        print('kernel_size: ', layer_config['kernel_size'])
        print('padding: ', layer_config['padding'])

    if layer_name.endswith('act'):
        print(colored('layer_name: ', 'cyan'), layer_name)
        print('activation: ', layer_config['activation'])
'''

# layer 내 config 확인 (3) - weight, bias
layer = model.layers[-2]
weight = layer.get_weights()[0]
bias = layer.get_weights()[1]
print(colored('type(weight): ', 'cyan'), type(weight))
print(colored('weight: ', 'cyan'), weight)
print(colored('weight.shape: ', 'cyan'), weight.shape)

print(colored('type(bias): ', 'cyan'), type(bias))
print(colored('bias: ', 'cyan'), bias)
print(colored('bias.shape: ', 'cyan'), bias.shape)

print('trainable params: ', np.prod(weight.shape)+np.sum(bias.shape))