import tensorflow as tf
import tensorflow.contrib.slim as slim
# Build a graph.

variables_to_restore = slim.get_variables_to_restore(exclude=["v1"])


labels = ['0','1','1','1','2','3','4']
num_classes = 5

ph_lables = tf.placeholder(tf.int32, [None], "my_placeholder")

res_onehot = slim.one_hot_encoding(ph_lables, num_classes)


# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    
    res = sess.run(res_onehot, feed_dict={ph_lables: labels})
    print(res)
    
   
    
   

    
   
 