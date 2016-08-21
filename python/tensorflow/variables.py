import tensorflow as tf

# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")

with tf.device("/cpu:0"):
    v = tf.Variable(tf.zeros([200]), name="biases")
    
# Pin a variable to GPU.
with tf.device("/gpu:0"):
  v = tf.Variable(tf.zeros([200]), name="biases")
  
with tf.device("/job:ps/task:7"):
  v = tf.Variable(tf.zeros([200]), name="biases")

#Create a variable with a random value.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
# Create another variable with the same value as 'weights'.
w2 = tf.Variable(weights.initialized_value(), name="w2")

# Create another variable with twice the value of 'weights'
w_twice = tf.Variable(weights.initialized_value() * 2.0, name="w_twice")
  
# Add an op to initialize the variables.
init_op = tf.initialize_all_variables()


# Later, when launching the model
with tf.Session() as sess:
  # Run the init operation.
  sess.run(init_op)
  # Use the model







