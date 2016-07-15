# import modules
import pandas as pd
import numpy as np

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                              'foo', 'bar', 'foo', 'foo'],
                       'B' : ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                     'C' : np.random.randn(8),
                      'D' : np.random.randn(8)})
                      

print df

byB = df.groupby(['B'])
# def f(group):
#     print 'ok'
#     return group.max()
# 
# res = byA.apply(f)
# print res

for name, group in byB:
    print name
    print group