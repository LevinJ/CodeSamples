import tensorflow as tf
import tensorflow.contrib.slim as slim
# Build a graph.


weights = slim.variable('weights',
                             shape=[10, 10, 3 , 3],
                             initializer=tf.truncated_normal_initializer(stddev=0.1),
                             regularizer=slim.l2_regularizer(0.05),
                             device='/CPU:0')

weights_2 = slim.model_variable('weights_2',
                              shape=[10, 10, 3 , 3],
                              initializer=tf.truncated_normal_initializer(stddev=0.1),
                              regularizer=slim.l2_regularizer(0.05),
                              device='/CPU:0')

my_var = slim.variable('my_var',
                       shape=[20, 1],
                       initializer=tf.zeros_initializer())
regular_variables_and_model_variables = slim.get_variables()

variables_to_restore = slim.get_variables_to_restore(exclude=["v1"])
# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    print(my_var.eval())
    print(weights.eval())
    
    
   

    
   
 