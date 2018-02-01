import tensorflow as tf


# s = tf.Variable(2.0)
# tx = tf.Variable(2.0)
# ty = tf.Variable(3.0)


x = tf.Variable([2.0, 5.0, 6.0])

s = x[0]
tx = x[1]
ty = x[2]


row_1 = tf.stack([s, 0.0, tx])
row_2 = tf.stack([0.0, s, ty])

theta = tf.stack([row_1,row_2])

# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    
    
    print(s.eval())
    print(row_1.eval())
    print(row_2.eval())
    print(theta.eval())