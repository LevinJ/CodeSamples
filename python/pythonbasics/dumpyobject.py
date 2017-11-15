import pandas as pd
import numpy as np
import json


filename = '/home/levin/workspace/snrprj/snr/data/process_result/train_pipeline.csv'

df = pd.read_csv(filename)

valid_blobs = np.unique(df['self.clf_valid_hsblobs'].values, return_counts=True)

vbdf = pd.DataFrame(np.array(valid_blobs).T, columns=['valid_balob', 'count'])


snr_count = (df['self.note_orientation'].values  != 3).sum()


des = df.describe()
with open("Output.txt", "w") as text_file:
    text_file.write("snr count: {}\n".format(snr_count))
    text_file.write("summary: {}\n".format(des.__str__))
    text_file.write("valid blobs: {}\n".format(vbdf.__str__))
print('done')
