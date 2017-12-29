import tensorflow as tf
import tensorflow.contrib.slim as slim
import matplotlib.pyplot as plt
import numpy as np
import math


raw_image = plt.imread('/home/levin/workspace/snrprj/snr/data/process_result/snrimgs/sample_test/batch_1/DOWN/20171017162233_F004F21727_top_right.jpg')
shape = raw_image.shape
raw_image = raw_image.reshape((1, shape[0], shape[1], 1))

# Build a graph.


input_image_placeholder = tf.placeholder(tf.uint8, shape = (None, None, None, 1))

intput_image = tf.image.convert_image_dtype(input_image_placeholder, dtype=tf.float32)
intput_image = tf.subtract(intput_image, 0.5)
intput_image = tf.multiply(intput_image, 2.0)

intput_image = tf.contrib.image.rotate(intput_image, 180 * math.pi / 180)

# intput_image = tf.image.flip_up_down(intput_image[0])

# Evaluate the tensor `c`.
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    res_img = sess.run(intput_image, feed_dict = {input_image_placeholder:raw_image})


row, col = 1,2
plt.subplot(row, col,1),plt.imshow(np.squeeze(raw_image), 'gray')
plt.subplot(row, col,2),plt.imshow(np.squeeze(res_img) , 'gray')
plt.show()
    
    
    
   

    
   
 