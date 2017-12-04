import tensorflow as tf
# Build a graph.

my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3], dtype=tf.int32, 
  initializer=tf.zeros_initializer)

other_variable = tf.get_variable("other_variable", dtype=tf.int32, 
  initializer=tf.constant([23, 42]))

my_local = tf.get_variable("my_local", shape=(), collections=[tf.GraphKeys.LOCAL_VARIABLES])
my_non_trainable = tf.get_variable("my_non_trainable", 
                                   shape=(), 
                                   trainable=False)
tf.add_to_collection("my_collection_name", my_local)

my_collection = tf.get_collection("my_collection_name")


v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())

w = tf.assign(tf.assign(v, 10), 1000)
# x = tf.assign(w, 100)




# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    
    sess.run(my_int_variable.initializer)
    
    print(w.eval())
    print(v.eval())
#     print(x.eval())
    

    
   
 