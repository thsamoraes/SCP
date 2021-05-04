import numpy as np
from matplotlib import pyplot as plt

a = 4
b = 7
t = np.linspace(-30,30,300)


def y(t):
    y = a*np.cos(t)
    x = b*np.sin(t)
    return x, y

x, y = y(t)

plt.plot()
plt.plot(x, y, 'r')
plt.scatter(0, 0, color='red')
plt.xlabel('x')
plt.ylabel('y')


plt.title('Plot de uma Elipse')

plt.grid()
