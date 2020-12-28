import tensorflow as tf

from utils.learning_env_setting import dir_setting, continue_setting, get_classification_metrics
from utils.dataset_utils import load_processing_mnist, load_processing_cifar10
from utils.train_validation_test import train, validation, test
from utils.checkpoint_utils import save_metrics_model, metric_visualizer
from utils.basic_utils import resetter, training_report

from leNet_impl_with_subclassing import LeNet5

'''
[Tensorflow2 강의] 28강 Training LeNet5 Revisited 강의 예제샘플
'''

''' === Learning Setting === '''
exp_name = 'LeNet5_train'
CONTINUE_LEARNING = True

train_ratio = 0.8
train_batch_size, test_batch_size = 128, 128

epochs = 10
save_period = 2
learning_rate = 0.01

model = LeNet5()
optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
''' === Learning Setting === '''

if __name__ == '__main__':
    path_dict = dir_setting(exp_name, CONTINUE_LEARNING)
    model, losses_accs, start_epoch = continue_setting(CONTINUE_LEARNING, path_dict, model=model)

    train_ds, validation_ds, test_ds = load_processing_mnist(train_ratio, train_batch_size, test_batch_size)
    metric_objects = get_classification_metrics()
    #print('metric_objects: {}'.format(metric_objects))

    for epoch in range(start_epoch, epochs):
        train(train_ds, model, loss_object, optimizer, metric_objects)
        validation(validation_ds, model, loss_object, metric_objects)

        training_report(epoch, losses_accs, metric_objects)
        save_metrics_model(epoch, model, losses_accs, path_dict, save_period)

        metric_visualizer(losses_accs, path_dict['cp_path'])
        resetter(metric_objects)

    test(test_ds, model, loss_object, metric_objects, path_dict)

