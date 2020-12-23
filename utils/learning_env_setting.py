import os
import shutil
from termcolor import colored
import numpy as np
import argparse

import tensorflow as tf
from tensorflow.keras.metrics import Mean, SparseCategoricalAccuracy

def argparser(epochs, learning_rate, train_batch_size):
    print('[argparser]', 'received parameter',
          'epochs: {}, learning_rate:{}, training_batch_size: {}'.format(epochs, learning_rate, train_batch_size))

    parser = argparse.ArgumentParser(description='hyper parameters for training')
    parser.add_argument('-e', type=int, default=None,
                        help='an integer for epochs')
    parser.add_argument('-l', type=float, default=None,
                        help='an floating point for learning rate')
    parser.add_argument('-b', type=int, default=None,
                        help='an integer for batch size')
    parser.add_argument('-a', type=str, default=None,
                        help='an string for activation function')
    parser.add_argument('-c', type=int, default=None,
                        help='an integer for experiment count')
    arg = parser.parse_args()

    if arg.e == None:
        epochs = epochs
    else:
        epochs = arg.e

    if arg.l == None:
        learning_rate = learning_rate
    else:
        learning_rate = arg.l

    if arg.b == None:
        train_batch_size = train_batch_size
    else:
        train_batch_size = arg.b

    if arg.a == None:
        activation = 'relu'
    else:
        activation = arg.a

    if arg.c == None:
        exp_idx = 0
    else:
        exp_idx = arg.c

    return exp_idx, epochs, learning_rate, train_batch_size, activation

def dir_setting(dir_name, CONTINUE_LEARNING):
    print('[dir_setting]',
          'dir_name: {}, CONTINUE_LEARNING:{}'.format(dir_name, CONTINUE_LEARNING))

    cp_path = os.path.join(os.getcwd(), dir_name)
    confusion_path = os.path.join(cp_path, 'confusion_matrix')
    model_path = os.path.join(cp_path, 'model')
    print('[dir_setting]',
          'cp_path: {}, confusion_path: {}, model_path: {}'.format(cp_path, confusion_path, model_path))

    if not CONTINUE_LEARNING and os.path.isdir(cp_path):
        shutil.rmtree(cp_path)

    if not os.path.isdir(cp_path):
        os.makedirs(cp_path, exist_ok=True)
        os.makedirs(confusion_path, exist_ok=True)
        os.makedirs(model_path, exist_ok=True)

    path_dict = dict()
    path_dict['cp_path'] = cp_path
    path_dict['confusion_path'] = confusion_path
    path_dict['model_path'] = model_path
    return path_dict

def get_classification_metrics(losses=None, accuracy=None):
    train_loss = Mean()
    train_acc = SparseCategoricalAccuracy()
    validation_loss = Mean()
    validation_acc = SparseCategoricalAccuracy()
    test_lost = Mean()
    test_acc = SparseCategoricalAccuracy()

    metrics_objects = dict()
    metrics_objects['train_loss'] = train_loss
    metrics_objects['train_accuracy'] = train_acc
    metrics_objects['validation_loss'] = validation_loss
    metrics_objects['validation_accuracy'] = validation_acc
    metrics_objects['test_loss'] = test_lost
    metrics_objects['test_accuracy'] = test_acc

    return metrics_objects

def continue_setting(CONTINUE_LEARNING, path_dict, model=None):
    print('[continue_setting]',
          'CONTINUE_LEARNING: {}, path_dict: {}, model: {}'.format(CONTINUE_LEARNING, path_dict, model))

    if CONTINUE_LEARNING and len(os.listdir(path_dict['model_path'])) == 0:
        CONTINUE_LEARNING = False
        print('[continue_setting]', colored('CONTINUE_LEARNING has been converted to False', 'cyan'))

    if CONTINUE_LEARNING:
        epoch_list = os.listdir(path_dict['model_path'])
        epoch_list = [int(epoch.split('_')[1]) for epoch in epoch_list]
        epoch_list.sort()

        last_epoch = epoch_list[-1]
        model_path = '{}/epoch_{}'.format(path_dict['model_path'], last_epoch)
        model = tf.keras.models.load_model(model_path)

        losses_accs_path = path_dict['cp_path']
        losses_accs_np = np.load(losses_accs_path + '/losses_accs.npz')
        losses_accs = dict()
        for k, v in losses_accs_np.items():
            losses_accs[k] = list(v)

        start_epoch = last_epoch + 1
    else:
        model = model
        start_epoch = 0
        losses_accs = dict()
        losses_accs['train_losses'] = []
        losses_accs['train_accuracies'] = []
        losses_accs['validation_losses'] = []
        losses_accs['validation_accuracies'] = []

    return model, losses_accs, start_epoch

if __name__ == '__main__':
    #dir_setting('train', True)

    metrics = get_classification_metrics()
    print('metrics.keys(): {}'.format(metrics.keys()))
    print('metrics.values(): {}'.format(metrics.values()))