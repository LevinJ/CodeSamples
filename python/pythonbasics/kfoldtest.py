from sklearn.cross_validation import KFold


kf = KFold(n=12, n_folds=3, shuffle=False,
                               random_state=None)

# for train_index, test_index in kf:
#     print("TRAIN:", train_index, "TEST:", test_index)

for x in kf:
    print("TRAIN:", x[0], "TEST:", x[1])
        
idset = [x[1] for x in kf]
nfold = len(idset)