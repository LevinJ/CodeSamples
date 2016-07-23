import tensorflow as tf
import numpy as np
import logging
from bokeh.util.logconfig import level
import sys


    
class TFModel(object):
    def __init__(self):
        self.num_steps = 200
        self.batch_size = 120
        return
    def get_input(self):
        pass
    def inference_operations(self):
        pass
    def loss_operation(self):
        return
    def optimize_operation(self):
        return
    def visualize_operation(self):
        return
    def __build_graph(self):
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.get_input()
            self.loss_operation()
            self.optimize_operation()
            self.inference_operations()
            self.visualize_operation()
        return
    def run_graph(self):
        return
    def run(self):
        self.__build_graph()
        self.run_graph()
        return
    
    
class IrisTFModel(TFModel):
    def __init__(self):
        TFModel.__init__(self)
#         tensorflow_log = logging.getLogger('tensorflow')
# 
#         tensorflow_log.handlers = [logging.NullHandler()]
#         
#         
#         _logger = logging.getLogger()
#         _logger.setLevel(logging.DEBUG)
#         _handler = logging.StreamHandler(sys.stdout)
#         _handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s  %(message)s  %(pathname)s%(filename)s:%(lineno)d %(funcName)s%(asctime)s", None))
#         _logger.addHandler(_handler)
        logging.basicConfig(level = logging.DEBUG)
        return
    def visualize_operation(self):
        with tf.name_scope('summaries'):
            tf.scalar_summary('loss', self.loss)
        with tf.name_scope('accuracy'):
            tf.scalar_summary('train_accuracy', self.train_accuracy)
            tf.scalar_summary('test_accuracy', self.train_accuracy)
            tf.histogram_summary("weight_hidden1", self.weight_hidden1)
            tf.histogram_summary("weight_output", self.weight_output)
            tf.histogram_summary("biases_hidden1", self.biases_hidden1)
            tf.histogram_summary("biases_output", self.biases_output)
        # Merge all the summaries and write them out to /tmp/mnist_logs (by default)
        self.merged = tf.merge_all_summaries()
        self.train_writer = tf.train.SummaryWriter('/tmp/iris_logs', self.graph)
        return
    def get_input(self):
        # Input data.
        # Load the training, validation and test data into constants that are
        # attached to the graph.
        IRIS_TRAINING = "iris_training.csv"
        IRIS_TEST = "iris_test.csv"
        training_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TRAINING, target_dtype=np.int)
        test_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TEST, target_dtype=np.int)

        self.x_train, self.x_test, self.y_train, self.y_test = training_set.data, test_set.data, \
        training_set.target, test_set.target
        
        self.x_train, self.x_test= self.x_train.astype(np.float32), self.x_test.astype(np.float32)
        
        num_labels = 3
        self.y_train = (np.arange(num_labels) == self.y_train[:,None]).astype(np.float32)
        self.y_test = (np.arange(num_labels) == self.y_test[:,None]).astype(np.float32)
        
        #placeholder
        self.tf_train_dataset = tf.placeholder(tf.float32,shape=(self.batch_size, 4))
        self.tf_train_labels = tf.placeholder(tf.float32, shape=(self.batch_size, 3))
        
        return
    def inference(self, input_dataset, keep_prob=1.0):
        input_num = 4
        hidden1_num = 10
#         hidden2_num = 20
#         hidden3_num = 10
        output_num = 3
        
        weight_hidden1 =  tf.Variable(tf.truncated_normal([input_num, hidden1_num],stddev=0.01))
        biases_hidden1 =  tf.Variable(tf.zeros([hidden1_num]))
        
#         weight_hidden2 =  tf.Variable(tf.truncated_normal([hidden1_num, hidden2_num]))
#         biases_hidden2 =  tf.Variable(tf.zeros([hidden2_num]))
#         
#         weight_hidden3 =  tf.Variable(tf.truncated_normal([hidden2_num, hidden3_num]))
#         biases_hidden3 =  tf.Variable(tf.zeros([hidden3_num]))
        
        weight_output =  tf.Variable(tf.truncated_normal([hidden1_num, output_num],stddev=0.01))
        biases_output =  tf.Variable(tf.zeros([output_num]))
        
        z_hidden1 = tf.matmul(input_dataset, weight_hidden1 ) + biases_hidden1
        relu1 = tf.nn.relu(z_hidden1)
        a_hidden1 = relu1
#         a_hidden1 = tf.nn.dropout(relu1, keep_prob)
        
#         z_hidden2 = tf.matmul(a_hidden1, weight_hidden2 ) + biases_hidden2
#         relu2 = tf.nn.relu(z_hidden2)
#         a_hidden2 = tf.nn.dropout(relu2, keep_prob)
#         
#         z_hidden3 = tf.matmul(a_hidden2, weight_hidden3 ) + biases_hidden3
#         relu3 = tf.nn.relu(z_hidden3)
#         a_hidden3 = tf.nn.dropout(relu3, keep_prob)
        
        z_output = tf.matmul(a_hidden1, weight_output ) + biases_output
        
        self.weight_hidden1 = weight_hidden1
        self.biases_hidden1 = biases_hidden1
        self.weight_output = weight_output
        self.biases_output = biases_output
        return z_output
    def loss_operation(self):
        inference_train = self.inference(self.tf_train_dataset)
        
        self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(inference_train, self.tf_train_labels))
        return
    
    def optimize_operation(self):
        self.optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(self.loss)
#         self.optimizer = tf.train.AdagradOptimizer(
#                             learning_rate=0.1).minimize(self.loss)
        return
    def inference_operations(self):
        self.train_prediction = tf.nn.softmax(self.inference(self.x_train))
        self.test_prediction = tf.nn.softmax(self.inference(self.x_test))
        self.train_accuracy = self.__get_accuracy(self.y_train, self.train_prediction)
        self.test_accuracy = self.__get_accuracy(self.y_test, self.test_prediction)
        return
    def __get_accuracy(self, y_true, y_pred):
        correct_prediction = tf.equal(tf.argmax(y_true, 1), tf.argmax(y_pred, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        return accuracy
    def accuracy(self, predictions, labels):
        return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))
          / predictions.shape[0])
    def run_graph(self):
        logging.debug("computeGraph")
        with tf.Session(graph=self.graph) as session:
            tf.initialize_all_variables().run()
            logging.debug("Initialized")
            for step in range(self.num_steps):
                _positions = np.random.choice(self.x_train.shape[0], size=self.batch_size, replace=False)
                batch_data = self.x_train[_positions, :]
                batch_labels = self.y_train[_positions,:]
                feed_dict = {self.tf_train_dataset : batch_data, self.tf_train_labels : batch_labels}
                _, l, predictions = session.run([self.optimizer, self.loss, self.train_prediction], feed_dict=feed_dict)
                if (step % 10 == 0):
                    logging.debug("Step {}/{}: loss{:.3f}   train/test {:.3f}/{:.3f}".format(step, 
                                                                                                    self.num_steps,l,self.train_accuracy.eval(),self.test_accuracy.eval()))
#                     logging.debug("Minibatch accuracy: {}".format(self.train_accuracy.eval()))
#                     logging.debug("Minibatch accuracy: %.1f%%" % self.accuracy(predictions, batch_labels))
#                     res = self.accuracy(self.test_prediction.eval(), self.y_test)
#                     logging.debug("Test accuracy: {}".format(self.test_accuracy.eval()))
                    summary = session.run(self.merged, feed_dict=feed_dict)
                    self.train_writer.add_summary(summary, step)
            res_test = self.accuracy(self.test_prediction.eval(), self.y_test)
            res_train = self.accuracy(self.train_prediction.eval(), self.y_train)
            logging.debug("Train accuracy: %.1f  Test accuracy: %.1f" % (res_train, res_test,))
        return


if __name__ == "__main__":   
    obj= IrisTFModel()
    obj.run()
