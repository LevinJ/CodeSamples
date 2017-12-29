import tensorflow as tf

from tensorflow.python.ops import math_ops


def character_accuracy(predictions, labels):
    """predictions and labels are of shape Batches x NUM_Digits
    """
    predictions, labels = pad_pred_label(predictions, labels)
    predictions.get_shape().assert_is_compatible_with(labels.get_shape())
    if labels.dtype != predictions.dtype:
        predictions = math_ops.cast(predictions, labels.dtype)
      
    is_correct = math_ops.to_float(math_ops.equal(predictions, labels))
    acc = tf.reduce_mean(is_correct)
    return acc
def pad_pred_label(predictions, labels):
    num_digit_predictions = tf.shape(predictions)[-1]
    num_digit_labels = tf.shape(labels)[-1]
    
    paddings_mask = tf.constant([[0,0], [0,1]])
    paddings = tf.fill([2,2], tf.abs(num_digit_predictions-num_digit_labels))
    paddings  = paddings * paddings_mask
    # paddings = tf.constant([[0, 0,], [0, tf.abs(num_digit_predictions-num_digit_predictions)]])
    
    predictions = tf.cond(num_digit_predictions< num_digit_labels, lambda: tf.pad(predictions, paddings, constant_values=-1), lambda: tf.identity(predictions))
    labels = tf.cond(num_digit_labels< num_digit_predictions, lambda: tf.pad(labels, paddings, constant_values=-1), lambda: tf.identity(labels))
    return predictions, labels

predictions = tf.constant([[1, 2], [4, 5]]) 
labels =  tf.constant([[1, 2, 3, 8], [4, 5, 6, 9]])






acc = character_accuracy(predictions, labels)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    np_acc, np_predictions, np_labels = sess.run([acc,predictions, labels])
    print(np_acc)
    print(np_predictions)
    print(np_labels)
    
    