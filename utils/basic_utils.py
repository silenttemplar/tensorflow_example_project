import tensorflow as tf
from termcolor import colored

def resetter(metric_objects):
    metric_objects['train_loss'].reset_states()
    metric_objects['train_accuracy'].reset_states()
    metric_objects['validation_loss'].reset_states()
    metric_objects['validation_accuracy'].reset_states()

def training_report(epoch, losses_accs, metric_objects, exp_name=None):
    train_loss = metric_objects['train_loss']
    train_accuracy = metric_objects['train_accuracy']
    validation_loss = metric_objects['validation_loss']
    validation_accuracy = metric_objects['validation_accuracy']

    losses_accs['train_losses'].append(train_loss.result().numpy())
    losses_accs['train_accuracies'].append(train_accuracy.result().numpy()*100)
    losses_accs['validation_losses'].append(validation_loss.result().numpy())
    losses_accs['validation_accuracies'].append(validation_accuracy.result().numpy()*100)

    if exp_name:
        print(colored('Exp: ', 'red', 'on_white'), exp_name)
    print(colored('Epoch', 'red', 'on_white'), epoch+1)

    template = 'Train Loss: {:.4f}, Train Accuracy: {:.2f}%\n' +\
                 'Validation Loss: {:.4f}, Validation Accuracy: {:.2f}%'
    print(template.format(losses_accs['train_losses'][-1], losses_accs['train_accuracies'][-1],
                          losses_accs['validation_losses'][-1], losses_accs['validation_accuracies'][-1]))

