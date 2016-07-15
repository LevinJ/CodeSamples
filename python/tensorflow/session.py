import tensorflow as tf
# Build a graph.
a = tf.constant(5.0)
b = tf.constant(6.0)
b2 = tf.constant(6.0)
b3 = tf.constant(6.0)
b4 = tf.constant(6.0)
c = a * b

# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    print(sess.run(c))
    print(c.eval())