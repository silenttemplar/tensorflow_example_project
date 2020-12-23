import tensorflow as tf

def train(train_ds, model, loss_object, optimizer, metric_objects):
    for images, labels in train_ds:
        with tf.GradientTape() as tape:
            predications = model(images)
            loss = loss_object(labels, predications)

        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

        metric_objects['train_loss'](loss)
        metric_objects['train_accuracy'](labels, predications)

def validation(validation_ds, model, loss_object, metric_objects):
    for images, labels in validation_ds:
        predications = model(images)
        loss = loss_object(labels, predications)

        metric_objects['validation_loss'](loss)
        metric_objects['validation_accuracy'](labels, predications)

def test(test_ds, model, loss_object, metric_objects, path_dict):
    for images, labels in test_ds:
        predications = model(images)
        loss = loss_object(labels, predications)

        metric_objects['test_loss'](loss)
        metric_objects['test_accuracy'](labels, predications)

    loss, acc = metric_objects['test_loss'].result().numpy(), metric_objects['test_accuracy'].result().numpy()
    with open('{}/test_result.txt'.format(path_dict['cp_path']), 'w') as f:
        template = 'test_loss:{},test_accuracy:{}'
        f.write(template.format(loss, acc*100))