from scipy.linalg import lstsq
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
y = np.array([-2.0, 0.5, -2.0, 1.0, -0.5, 1.0])

N = 6

V = np.vander(x, N)

p, res, rnk, s = lstsq(V, y)

f = np.polyval(p, x)


plt.plot(x,y,'*',label='data')
plt.plot(x,f,label='fit')
plt.legend(loc=2, shadow=True)
plt.show()
