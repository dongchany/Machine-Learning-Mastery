from scipy.stats import norm
from matplotlib import pyplot

mu = 50
sigma = 5
dist = norm(mu, sigma)
values = [value for value in range(30, 70)]
probabilities = [dist.pdf(value) for value in values]
pyplot.plot(values, probabilities)
pyplot.show()

cprobs = [dist.cdf(value) for value in values]
pyplot.plot(values, cprobs)
pyplot.show()

low_end = dist.ppf(0.025)
hight_end= dist.ppf(0.975)
print('Middle 95%% between %.1f and %.1f' % (low_end, hight_end))
