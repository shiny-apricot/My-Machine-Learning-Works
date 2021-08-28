
import matplotlib.pyplot as plt
import seaborn as sns
import time
from tensorflow import keras
import tensorflow as tf

# updatable plot
# a minimal example (sort of)
from IPython.display import clear_output


class PlotLosses(tf.keras.callbacks.Callback):
    #
    def plot_figure(self, logs):
        plt.figure(figsize=(20,8))
        plt.grid(True)
        ##
        plt.subplot(1, 2, 1)
        sns.lineplot(x=self.x, y=self.losses, label="loss", size= self.lr)
        sns.lineplot(x=self.x, y=self.val_losses, label="val_loss", size= self.lr)
        plt.title('loss')
        plt.legend()
        ##
        plt.subplot(1, 2, 2)
        sns.lineplot(x=self.x, y=self.accuracy, label="accuracy", size= self.lr)
        sns.lineplot(x=self.x, y=self.val_accuracy, label="val_accuracy", size= self.lr)
        plt.title('accuracy')
        plt.legend()
        ##
        clear_output(wait=True)
        plt.show();
        self.current_time = time.time()
        accuracy = round(logs.get('accuracy'),4)
        print('ACCURACY=',accuracy)
        val_accuracy = round(logs.get('val_accuracy'), 4)
        print('VAL_ACCURACY=',val_accuracy)
    #
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.accuracy = []
        self.lr = []
        self.val_accuracy = []
        self.fig = plt.figure()
        self.logs = []
        self.current_time = time.time()
    #
    def on_epoch_end(self, epoch, logs={}):
        lr = float(tf.keras.backend.get_value(self.model.optimizer.learning_rate))
        lr = round(lr,6)
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.accuracy.append(logs.get('accuracy'))
        self.val_accuracy.append(logs.get('val_accuracy'))
        self.lr.append(lr)
        self.i += 1
        ##
        if time.time() - self.current_time > 2:
            self.plot_figure(logs)
        return plt
    #
    def on_train_end(self, logs=None):
        self.plot_figure()

    #Callback Source = https://gist.github.com/stared/dfb4dfaf6d9a8501cd1cc8b8cb806d2e