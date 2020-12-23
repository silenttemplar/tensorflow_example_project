import os
import shutil
from termcolor import colored
import tensorflow as tf
import numpy as np

from tensorflow.keras.metrics import Mean, SparseCategoricalAccuracy

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