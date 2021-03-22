import numpy as np

print("Vamos verificar se (cos(x) + isin(x))^n = cos(nx) + isin(nx)")
x = float(input("Digite um valor real para x: "))
n = int(input("Digite um valor inteiro para n: "))

def F3(x,n):
    return ((np.cos(x) + 1j*np.sin(x))**n)

def F4(x,n):
    return (np.cos(n*x) + 1j*np.sin(n*x))

if F3(x,n) == F4(x,n):
    print("A equação se verifica!")
else:
    print ("A equação não se verifica")
    
# está retornando falso para quaisquer pares (x, n)
