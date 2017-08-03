# load up some dataset. Could be anything but skdata is convenient.
# from skdata.mnist.views import OfficialVectorClassification
import skdata
from tqdm import tqdm
import numpy as np
import tensorflow as tf

data = OfficialVectorClassification()
trIdx = data.sel_idxs[:]

# one MUST randomly shuffle data before putting it into one of these
# formats. Without this, one cannot make use of tensorflow's great
# out of core shuffling.
np.random.shuffle(trIdx)


writer = tf.python_io.TFRecordWriter("mnist.tfrecords")
# iterate over each example
# wrap with tqdm for a progress bar
for example_idx in tqdm(trIdx):
    features = data.all_vectors[example_idx]
    label = data.all_labels[example_idx]

    # construct the Example proto boject
    example = tf.train.Example(
        # Example contains a Features proto object
        features=tf.train.Features(
          # Features contains a map of string to Feature proto objects
          feature={
            # A Feature contains one of either a int64_list,
            # float_list, or bytes_list
            'label': tf.train.Feature(
                int64_list=tf.train.Int64List(value=[label])),
            'image': tf.train.Feature(
                int64_list=tf.train.Int64List(value=features.astype("int64"))),
    }))
    # use the proto object to serialize the example to a string
    serialized = example.SerializeToString()
    # write the serialized object to disk
    writer.write(serialized)