import numpy as np
from matplotlib import pyplot as plt

#1

h = 1/1000

a = -0.5

n = 0

u = [np.exp(0),np.exp(h*a),np.exp(2*h*a)]

for n in range(997):
    x = (u[n + 2] + h*a*(23/12)*u[n + 2] - h*a*(4/3)*u[n + 1] + h*a*(5/12)*u[n + 0])
    u.append(x)

print(u)


#2a 

m=0

td = []

for m in range(1000):
    y = m*h
    td.append(y)
    
print(td)

plt.plot(td,u)

#2b

p = 0

L = []

for p in range (1000):
    z = abs(u[p] - td[p])
    L.append(z)

plt.plot(td,L)
