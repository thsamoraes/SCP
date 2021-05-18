import numpy as np

def f(x):
    return 1 / np.sqrt(x)
   
lista = []

for i in np.arange(1,200,1):
    lista.append(f(i))

print(lista)    
print("A soma da lista é: ",sum(lista))
