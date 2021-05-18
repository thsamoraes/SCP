print("Faremos operações entre um número real e um intervalo do tipo [a,b].")
q = float(input(print("Digite um número inteiro: q = ")))
A = int(input(print("Digite o começo do intervalo: a = ")))
B = int(input(print("Digite o final do intervalo: b = ")))
N = int(input(print("Digite um número inteiro para ser usado na potenciação: ")))

class Interval:
    def __init__(self, a, b, c, d, n):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.n = n
        
    def __add__(self):
        return [self.a + self.c, self.b + self.d]
        
    def __sub__(self):
        return [self.a - self.d, self.b - self.c]
        
    def __truediv__(self):
        if (self.c == 0 or self.d == 0):
            print("Dividindo por zero") 
        else: 
            return [min(self.a/self.c, self.a/self.d, self.b/self.c, self.b/self.d), max(self.a/self.c, self.a/self.d, self.b/self.c, self.b/self.d)]
        
    def __mul__(self):
        return [min(self.a*self.c, self.a*self.d, self.b*self.c, self.b*self.d), max(self.a*self.c, self.a*self.d, self.b*self.c, self.b*self.d)]
        
    def __pow__(self):
        return [self.a**self.n,self.b**self.n]
    
test = Interval(A,B,q,q,N)

print("Fazendo a operação [",A,",",B,"] +",q,".Temos: \n",test.__add__())
print("\nFazendo a operação [",A,",",B,"] -",q,".Temos: \n",test.__sub__())
print("\nFazendo a operação [",A,",",B,"] /",q,".Temos: \n",test.__truediv__())
print("\nFazendo a operação [",A,",",B,"] *",q,".Temos: \n",test.__mul__())
print("\nFazendo a operação [",A,",",B,"] ^",N,".Temos: \n",test.__pow__())
