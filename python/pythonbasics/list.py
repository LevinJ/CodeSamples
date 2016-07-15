import numpy as np
import pandas as pd
# a= [1,1,2,5,5]
# m = max(a)
# maxindexes =  [i for i, j in enumerate(a) if j == m]
# print maxindexes
# print np.random.choice(maxindexes)


a = pd.Series(['2016-01-22-46', '2016-01-22-58'])
print a.map(lambda x: "-".join(x.split('-')[:3] + [x.split('-')[-1].zfill(3)]))