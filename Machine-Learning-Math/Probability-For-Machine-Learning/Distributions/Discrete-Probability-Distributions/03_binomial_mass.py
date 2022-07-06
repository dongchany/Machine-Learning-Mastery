from scipy.stats import binom

p = 0.3
k = 100
dist = binom(k, p)
for n in range(10, 110, 10):
    print('P of %d success: %.3f%%' % (n, dist.pmf(n)*100))
