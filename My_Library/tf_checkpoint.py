
from tensorflow import keras
import tensorflow as tf


def checkpoint_generator(name='model'):
    n1 = str(name) + '_valacc.tf'
    n2 = str(name) + '_valloss.tf'
    cp_val_accuracy = tf.keras.callbacks.ModelCheckpoint(n1,save_best_only=True,
                                                   monitor="val_accuracy")

    cp_val_loss = tf.keras.callbacks.ModelCheckpoint(n2,save_best_only=True,
                                                   monitor="val_loss")

    return cp_val_accuracy, cp_val_loss

def checkpoint_evaluate(name, **kwargs):
    if 'x' not in kwargs and 'y' not in kwargs:
        raise NameError('"x" and "y" values are missing.')
        return False
    ##
    name_list = []
    name_list.append(str(name) + '_valacc.tf')
    name_list.append(str(name) + '_valloss.tf')
    ##
    model_list = []
    for name in name_list:
        model_list.append(tf.keras.models.load_model(name))
    ##
    result_list = []
    for number, model in enumerate(model_list):
        if 'x' in kwargs and 'y' in kwargs:
            try:
                print(name_list[number])
                result = model.evaluate(kwargs['x'], kwargs['y'])
                result_list.append(result)
                print()
            except:
                print('Could not evaluate the', name_list(number))
        ##
        if 'x' in kwargs and 'y' not in kwargs:
            try:
                print(name_list[number])
                result = model.evaluate(kwargs['x'])
                result_list.append(result)
                print()
            except:
                print('Could not evaluate the', name_list(number))
    ##
    return result_list