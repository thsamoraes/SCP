import numpy as np

A = [[2, 11, 5e-17],
     [-5, 9e-17, -7e-17]]

print("Matriz Inicial: ")
print(A)


def cast2array(f):
    def new_function(obj):
        fA = f(np.array(obj))
        return fA
    return new_function


def g(A):
    tol = 1e-16
    A[np.abs(A) < tol] = 0.0
    print("Matriz Modificada: ")
    print(A)
    return A


def how_sparse(A):
    return len(A.reshape(-1).nonzero()[0])

g = cast2array(g)

how_sparse = cast2array(how_sparse)

print(how_sparse(g(A)))
