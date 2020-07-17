import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
print(fig, type(fig))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(np.random.randn(20).cumsum(), 'r--')
ax1.hist(np.random.randn(200), bins=20, color='g', alpha=1)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()

fig, axes = plt.subplots(2, 2)
print(type(fig), type(axes))
axes[0, 0].hist(np.random.randn(500), bins=10, color='b', alpha=0.5)
axes[1, 1].scatter(np.arange(30),
                   np.arange(30) + 2 * np.log(10) * np.random.randn(30))
plt.show()
