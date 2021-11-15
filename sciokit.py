import sklearn.preprocessing as preprocessing

x = [[0, 0], [0, 1], [2,0]]
enc = preprocessing.OneHotEncoder()
print(enc.fit(x).transform([[1, 1]]).toarray())