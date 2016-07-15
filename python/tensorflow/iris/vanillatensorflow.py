import tensorflow as tf


class TFModel:
    def __init__(self):
        return
    def get_input(self):
        return
    def inference_operations(self):
        return
    def loss_operation(self):
        return
    def optimize_operation(self):
        return
    def __build_graph(self):
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.inference_operations()
            self.loss_operation()
            self.optimize_operation()
        return
    def run_graph(self):
        return
    def run(self):
        self.get_input()
        self.__build_graph()
        self.run_graph()
        return
    
    




if __name__ == "__main__":   
    obj= TFModel()
    obj.run()