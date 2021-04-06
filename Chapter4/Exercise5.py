import numpy as np
import matplotlib.pyplot as plt


#1
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])

N = 6

V = np.vander(x, N)


A = V[:,1:]

print("V = \n",V)
print("Shape: ",np.shape(V))
print("A = \n",A)
print("Shape: ",np.shape(A))


#2

B = np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T)

print("B = \n",B)
print("Shape: ",np.shape(B))

#3 
y = np.array([-2.,0.5,-2.,1.,-0.5,1.])

c = np.dot(B,y)

print("c = ", c)
print("Shape: ",np.shape(c))

#4

f = np.polyval(c, x)

plt.plot(x,y,'*',label='y (x)')
plt.plot(x,f,label='f (x)')
plt.legend(loc=2, shadow=True)
plt.show()
