import tensorflow as tf



# v = tf.Variable(10)
# w = v.assign_add(10)




value = tf.Variable(tf.ones_initializer()(()))
value2 = value+3
print(tf.get_default_graph().as_graph_def())

sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
#     sess.run(v.initializer)
#     print(v.eval())
#     result = sess.run(w)
#     print(result)  # =
#     print(v.eval())
    