# Ex. 4 → Suppose we are trying to check the convergence of a 
# diverging sequence (here the sequence is defined by the recursive relation 
# u_n+1 = 2u_n and u_0 = 1.0):

u = 1.0 # you have to use a float here!
uold = 10.0

for iteration in range(2000):
    if abs(u-uold) > 1.e-8:
        print('Convergence')
        break # sequence has converged
    uold = u
    u = 2*u
else:
    print('No convergence')

# 1. prints 'Convergence'
# 2. prints 'No convergence'
# 3. não mudou ??
