import tensorflow as tf

from utils.learning_env_setting import dir_setting, continue_setting, get_classification_metrics, argparser
from utils.dataset_utils import load_processing_mnist
from utils.train_validation_test import train, validation, test
from utils.checkpoint_utils import save_metrics_model, metric_visualizer
from utils.basic_utils import resetter, training_report

from example.tensorflow2.leNet_impl_with_subclassing import LeNet5

''' === Learning Setting === '''
CONTINUE_LEARNING = True

train_ratio = 0.8
train_batch_size, test_batch_size = 128, 128

epochs = 10
save_period = 2
learning_rate = 0.01

exp_idx, epochs, learning_rate, train_batch_size, activation = argparser(epochs=epochs,
                                                                         learning_rate=learning_rate,
                                                                         train_batch_size=train_batch_size)

exp_name = 'exp{}_{}_LeNet5'.format(exp_idx, 'learning_rate')
base_dir = 'tensorflow2/'+exp_name

model = LeNet5(activation=activation)
optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
''' === Learning Setting === '''

loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
path_dict = dir_setting(base_dir, CONTINUE_LEARNING)
model, losses_accs, start_epoch = continue_setting(CONTINUE_LEARNING, path_dict, model=model)

train_ds, validation_ds, test_ds = load_processing_mnist(train_ratio, train_batch_size, test_batch_size)
metric_objects = get_classification_metrics()
# print('metric_objects: {}'.format(metric_objects))

for epoch in range(start_epoch, epochs):
    train(train_ds, model, loss_object, optimizer, metric_objects)
    validation(validation_ds, model, loss_object, metric_objects)

    training_report(epoch, losses_accs, metric_objects)
    save_metrics_model(epoch, model, losses_accs, path_dict, save_period)

    metric_visualizer(losses_accs, path_dict['cp_path'])
    resetter(metric_objects)

test(test_ds, model, loss_object, metric_objects, path_dict)



