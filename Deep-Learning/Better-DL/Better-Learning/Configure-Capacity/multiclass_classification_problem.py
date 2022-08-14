from matplotlib import pyplot
from sklearn.datasets import make_blobs
from numpy import where

X, y = make_blobs(n_samples=1000, centers=3, n_features=2, cluster_std=2, random_state=2)

for class_value in range(3):
    row_ix = where(y == class_value)
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])

pyplot.show()
