import numpy as np 

print("Vamos verificar se exp(ix) = cos(x) + isin(x)")
x = float(input("Digite um valor real para x: "))

def F5(x):
    return np.exp(1j*x)

def F6(x):
    return (np.cos(x) + 1j*np.sin(x))

if F5(x) == F6(x):
    print("A equação se verifica!")
else:
    print ("A equação não se verifica")
