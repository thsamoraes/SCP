import numpy as np

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

def ged(a,b):
    if a > b:
        x = b
    else:
        x = b
    while x > 1:
        if a % x == 0 and b % x == 0:
            break
        x = x - 1
    return x

print("\nO máximo divisor comum entre", a,"e", b,"é:",ged(a,b))


def lcm(a,b):
    y = int(abs(a*b)/ged(a,b))
    return y

print("\nO mínimo multiplo comum entre", a,"e", b,"é:",lcm(a,b))
