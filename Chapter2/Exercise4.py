u = 1
uold = 10

for iteration in range(2000):
    if not abs(u-uold) > 1.e-8:
        print('Convergence')
        break # sequence has converged
    uold = u
    u = 2*u
else:
    print('No convergence')

# Quando fazemos a série com números inteiros, podemos computar a quantidade 
# de números que a memória do computador aguenta, mas quando fazemos com float 
# ele nos dá infinito e a comparação de infinito dará nan que retorna falso 
# quando é comparado.
