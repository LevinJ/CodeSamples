import json
import numpy as np

data = {}
data['a'] = np.arange(10).tolist()
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)