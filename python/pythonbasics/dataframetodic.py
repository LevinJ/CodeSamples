import pandas as pd
data = [['p',1,3,2], ['q',4,3,2], ['r',4,0,9]]
df = pd.DataFrame(data, columns= ['ID', 'A', 'B', 'C'])
print df.to_dict('index')