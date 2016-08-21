import pandas as pd
import numpy as np

df = pd.DataFrame({ 'A' : 1.,
   'B' : pd.Timestamp('20130102'),
   'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
   'D' : np.array([3] * 4,dtype='int32'),
   'E' : pd.Categorical(["test","train","test","train"]),
   'F' : 'foo' })

def process_item(item, arg1, arg2, passed_key_arg=None):
    item = item.astype(str)
    print item
    return '_'.join(item)
res = df.apply(process_item, axis=1,args=(1,'good'), passed_key_arg = 10)
df['combined'] = df[['B','F']].apply((lambda x: '_'.join(x.astype(str))), axis=1)
print res

#column ITERATION_LIMIT

df['newstuff'] = []