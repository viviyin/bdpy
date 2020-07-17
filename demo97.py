import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

mu = 80
sigma = 8
x = mu + sigma * np.random.randn(10000)
print(len(x))
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue')
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r*--')

plt.show()
