import numpy as np
from scipy.linalg import lu

def Matriz(ordem):
    return np.full((ordem,ordem), -1, dtype=int)

ordem = int(input("Insira a ordem da sua matriz:  "))

Matriz = Matriz(ordem)

for i in range(1,ordem+1):
    for j in range(1,ordem+1):
        if (i<j and j!=ordem):
            Matriz[i-1][j-1] = 0
        elif (i==j or j==ordem):
            Matriz[i-1][j-1] = 1

print("Sua matriz é \n", Matriz)

P, L, U = lu(Matriz)

print("A matriz permutação é \n", P)
print("A matriz triangular inferior é \n", L)
print("A matriz triangular superior é \n", U)

growthfactor = (np.max( np.abs(U)))/(np.max (np.abs(Matriz)))

print("O fator de crescimento é: ", growthfactor)

# O fator de crescimento cresce com 2^(i+1)
