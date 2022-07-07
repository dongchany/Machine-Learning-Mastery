from numpy.random import randn
from matplotlib import pyplot

data = 5 * randn(10000) + 50
pyplot.hist(data, bins=200)
pyplot.show()
