from tensorboard.compat import tf
import sys
print(sys.path)
print(tf)
logdir = "/home/levin/workspace/CodeSamples/python/torch_test/run2/"
print(tf.io.__file__)
# tf.io.gfile.makedirs(logdir)