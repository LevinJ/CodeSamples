import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.monitors   import ValidationMonitor
# from tensorflow.python.platform import tf_logging as logging

# logging.set_verbosity(logging.INFO)
import logging
# logging.basicConfig(level = logging.INFO)
import sys

tensorflow_log = logging.getLogger('tensorflow')
tensorflow_log.handlers = [logging.NullHandler()]


_logger = logging.getLogger()
_logger.setLevel(logging.INFO)
# 
# 
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT, None))
# _handler.setLevel(logging.INFO)
_handler.addFilter(logging.Filter("tensorflow.contrib.learn.python.learn.monitors"))

# 
# 
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

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)

# Fit model.
classifier.fit(x=x_train, y=y_train, steps=200, monitors=[ValidationMonitor( x=x_test, y=y_test,every_n_steps=30)])

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=x_test, y=y_test)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new flower samples.
new_samples = np.array(
    [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))