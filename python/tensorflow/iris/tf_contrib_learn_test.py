import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.monitors   import ValidationMonitor
# from tensorflow.python.platform import tf_logging as logging

# logging.set_verbosity(logging.INFO)
import logging
# logging.basicConfig(level = logging.INFO)
import sys




tensorflow_log = logging.getLogger('tensorflow')
# tensorflow_log.setLevel(logging.DEBUG)
# tensorflow_log.
tensorflow_log.handlers = [logging.NullHandler()]


_logger = logging.getLogger()
_logger.setLevel(logging.DEBUG)
# 
# 
_handler = logging.StreamHandler(sys.stdout)
# _handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s  %(message)s", None))
_handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s  %(message)s  %(pathname)s%(filename)s:%(lineno)d %(funcName)s%(asctime)s", None))
# # _handler.setLevel(logging.INFO)
# _handler.addFilter(logging.Filter("tensorflow.contrib.learn.python.learn.monitors"))
# 
# # 
# # 
_logger.addHandler(_handler)




# logging.set_verbosity(logging.INFO)
# Data sets
IRIS_TRAINING = "iris_training.csv"
IRIS_TEST = "iris_test.csv"

# Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TRAINING, target_dtype=np.int)
test_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TEST, target_dtype=np.int)

x_train, x_test, y_train, y_test = training_set.data, test_set.data, \
  training_set.target, test_set.target
  
  

model_dir = '/tmp/myiris_model_val'
# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10], n_classes=3)

# classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)
# classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10], 
#                                             n_classes=3, optimizer=tf.train.GradientDescentOptimizer(0.1))

# class ValidationMonitor2(tf.contrib.learn.monitors.EveryN):
#     def __init__(self, every_n_steps=100):
#         tf.contrib.learn.monitors.EveryN.__init__(self,every_n_steps=100, first_n_steps=1)
#         return
#     def every_n_step_end(self, step, outputs):
#         logging.debug("step {}: ".format(step))
#         return False


# example_monitor = ValidationMonitor2()

monitor = ValidationMonitor(x= x_test, y=y_test, every_n_steps=1)
# Fit model.
classifier.fit(x=x_train, y=y_train, steps=10, monitors=[monitor])
# classifier.fit(x=x_train, y=y_train, steps=150)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=x_test, y=y_test)["accuracy"]
accuracy_score_train = classifier.evaluate(x=x_train, y=y_train)["accuracy"]
print('Test Accuracy: {}, Train Accuracy: {}'.format(accuracy_score, accuracy_score_train))

# Classify two new flower samples.
new_samples = np.array(
    [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))