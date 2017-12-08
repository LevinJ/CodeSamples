from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import tensorflow as tf
import tensorflow.contrib.slim as slim

from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.framework import sparse_tensor
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import check_ops
from tensorflow.python.ops import confusion_matrix
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn
from tensorflow.python.ops import sets
from tensorflow.python.ops import sparse_ops
from tensorflow.python.ops import state_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.ops import weights_broadcast_ops

# Build a graph.

def _local_variable(initial_value, validate_shape=True, name=None):
  """Create variable and add it to `GraphKeys.LOCAL_VARIABLES` collection.

  Args:
    initial_value: See variables.Variable.__init__.
    validate_shape: See variables.Variable.__init__.
    name: See variables.Variable.__init__.
  Returns:
    New variable.
  """
  return variable_scope.variable(
      initial_value, trainable=False,
      collections=[ops.GraphKeys.LOCAL_VARIABLES],
      validate_shape=validate_shape, name=name)

def _create_local(name, shape, collections=None, validate_shape=True,
                  dtype=dtypes.float32):
  """Creates a new local variable.

  Args:
    name: The name of the new or existing variable.
    shape: Shape of the new or existing variable.
    collections: A list of collection names to which the Variable will be added.
    validate_shape: Whether to validate the shape of the variable.
    dtype: Data type of the variables.

  Returns:
    The created variable.
  """
  # Make sure local variables are added to tf.GraphKeys.LOCAL_VARIABLES
  collections = list(collections or [])
  collections += [ops.GraphKeys.LOCAL_VARIABLES]
  return variable_scope.variable(
      lambda: array_ops.zeros(shape, dtype=dtype),
      name=name,
      trainable=False,
      collections=collections,
      validate_shape=validate_shape)

def _safe_div(numerator, denominator, name):
  """Divides two values, returning 0 if the denominator is <= 0.

  Args:
    numerator: A real `Tensor`.
    denominator: A real `Tensor`, with dtype matching `numerator`.
    name: Name for the returned op.

  Returns:
    0 if `denominator` <= 0, else `numerator` / `denominator`
  """
  return array_ops.where(
      math_ops.greater(denominator, 0),
      math_ops.truediv(numerator, denominator),
      0,
      name=name)
  
def steaming_mean(values):
    with variable_scope.variable_scope('mean'):
        values = math_ops.to_float(values)
    
        total = _create_local('total', shape=[])
        count = _create_local('count', shape=[])
    
        
        num_values = math_ops.to_float(array_ops.size(values))
        
    
        update_total_op = state_ops.assign_add(total, math_ops.reduce_sum(values))
        with ops.control_dependencies([values]):
            update_count_op = state_ops.assign_add(count, num_values)
    
        mean_t = _safe_div(total, count, 'value')
        update_op = _safe_div(update_total_op, update_count_op, 'update_op')
    
        return mean_t, update_op,total,count

my_values = tf.get_variable("other_variable", dtype=tf.int32, initializer=tf.constant([10, 20]))

add_ops = tf.assign(my_values, tf.constant([100, 100]))


values_op, update_op,total,count = steaming_mean(my_values)


# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    
    res = sess.run(update_op)
    print(res)
    print(sess.run([total, count]))
    print(sess.run(add_ops))
    print(sess.run([total, count]))
    res = sess.run(update_op)
    print(res)
    print(sess.run([total, count]))
    res = sess.run(values_op)
    print(res)
    
   

    
   
 