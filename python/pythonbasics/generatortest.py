import numpy as np

def generator(samples, batch_size=32):
        num_samples = len(samples)
        while 1: # Loop forever so the generator never terminates
            for offset in range(0, num_samples, batch_size):
                batch_samples = samples[offset:offset+batch_size]
                yield batch_samples

samples = np.arange(100)
our_generator = generator(samples)
my_output = []

for i in range(10):
    print((next(our_generator)))