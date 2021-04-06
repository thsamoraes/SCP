import numpy as np

v = np.array([[1.],[-1.],[1.]])
print("v = \n",v)
print("\nv transposto (v^T) = \n",v.T)

P = np.matmul(v,v.T)/np.matmul(v.T,v)

I = np.identity(3)

Q = I - P

print("\nP = \n",P)

print("\nQ = \n",Q)


print('\nP*v = \n', np.matmul(P,(v)))

print('v é autovetor de P com autovalor 1')


print('\nQ*v = \n', np.matmul(Q,(v)))

print('v é autovetor de Q com autovalor 0')
