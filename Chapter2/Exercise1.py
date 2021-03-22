def F2(x):
    return (x**2 + 0.25*x - 5)

print("Dada a expressão f(x) = x^2 + 0.25x - 5")

y = float(input("Digite um valor para x: "))

if F2(y) == 0:
    print(y,"é um zero da função!")
else:
    print(y,"não é um zero da função.")
