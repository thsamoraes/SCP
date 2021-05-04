import numpy as np
from matplotlib import pyplot as plt

f = lambda x: 3*x**2 - 5

x = np.arange(-5, 5, .05)

def bisec(f, a, b, tol):
       
    if f(a)*f(b) >= 0 :
        print("não há raíz no intervalo")
        
    medio = (a + b)/2
    
    if np.abs(f(medio)) < tol:
        return medio
    
    elif np.sign(f(a)) == np.sign(f(medio)):
        return bisec(f, medio, b, tol)
    
    elif np.sign(f(b)) == np.sign(f(medio)):
        return bisec(f, a, medio, tol)
