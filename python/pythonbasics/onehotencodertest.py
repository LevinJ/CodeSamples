from sklearn.preprocessing import OneHotEncoder


enc = OneHotEncoder()

enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])  


enc.n_values_

enc.feature_indices_

temp = enc.transform([[0, 1, 1], [0,0,0]])
print 'ok'
