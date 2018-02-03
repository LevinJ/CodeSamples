import tensorflow as tf

from tensorflow.python.ops import math_ops
import numpy as np


def character_accuracy(predictions, labels):
    """predictions and labels are of shape Batches x NUM_Digits_Pred and Batches x NUM_Digits_Label
    """
    if labels.dtype != predictions.dtype:
        predictions = math_ops.cast(predictions, labels.dtype)
    predictions, labels = pad_pred_label(predictions, labels)
    predictions.get_shape().assert_is_compatible_with(labels.get_shape())
    
      
    is_correct = math_ops.to_float(math_ops.equal(predictions, labels))
    acc = tf.reduce_mean(is_correct)
    return acc
def pad_pred_label(predictions, labels):
    num_digit_predictions = tf.shape(predictions)[-1]
    num_digit_labels = tf.shape(labels)[-1]
    
    paddings_mask = tf.constant([[0,0], [0,1]], dtype=labels.dtype)
    paddings = tf.cast(tf.fill([2,2], tf.abs(num_digit_predictions-num_digit_labels)),labels.dtype)
    paddings  = paddings * paddings_mask
    # paddings = tf.constant([[0, 0,], [0, tf.abs(num_digit_predictions-num_digit_predictions)]])
    
    predictions = tf.cond(num_digit_predictions< num_digit_labels, lambda: tf.pad(predictions, paddings, constant_values=-1), lambda: tf.identity(predictions))
    labels = tf.cond(num_digit_labels< num_digit_predictions, lambda: tf.pad(labels, paddings, constant_values=-1), lambda: tf.identity(labels))
    return predictions, labels


# np_predictions = np.arange(32*10).reshape([32,10])
# np_labels = np.arange(32*10).reshape([32,10])
# np_predictions[0][0] = -1

b = 32
m = 10
np_predictions = np.arange(b*m).reshape([b,m])
np_labels = np.arange(b*m).reshape([b,m])

predictions = tf.constant(np_predictions) 
labels =  tf.constant(np_labels)






acc = character_accuracy(predictions, labels)
# acc = tf.Print(acc, [predictions], 'data',summarize=320)

# acc = tf.cond(acc>=0.996876, lambda: tf.Print(acc, [predictions], "predictions=",summarize=320), lambda:tf.identity(acc))
# acc = tf.cond(acc>=0.996876, lambda: tf.Print(acc, [labels], "labels=",summarize=320), lambda:tf.identity(acc))
MAX = 0.996876
MAX = 1
acc = tf.cond(acc>MAX, lambda: tf.Print(acc, [predictions], "predictions=",summarize=320), lambda:tf.identity(acc))
acc = tf.cond(acc>MAX, lambda: tf.Print(acc, [labels], "labels=",summarize=320), lambda:tf.identity(acc))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    
    np_acc= sess.run([acc])
    print(np_acc)
#     print(np_predictions)
#     print(np_labels)
    
    