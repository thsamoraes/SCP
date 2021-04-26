import numpy as np

r = float(input("Digite um número real: "))
phi = float(input("Digite um ângulo: "))

def polar_to_comp(r,phi):
    z = r*np.exp(1j*phi)
    return z

print("\nO número complexo formado por r =",r,"e phi =",phi,"é z =","{:.2f}".format(polar_to_comp(r,phi)))
