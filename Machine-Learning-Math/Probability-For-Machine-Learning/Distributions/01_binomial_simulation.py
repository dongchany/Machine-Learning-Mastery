from numpy.random import binomial

p = 0.3
k = 100
success = binomial(k, p)
print('Total Success: %d' % success)
