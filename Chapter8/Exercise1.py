N = int(input("Digite o númerador da fração: "))
D = int(input("Digite o denominador da fração: "))

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def simplify(self):
        a = self.numerator
        b = self.denominator
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
        n_simp = self.numerator/ged(a,b)
        d_simp = self.denominator/ged(a,b)
        return (n_simp,d_simp)

q = RationalNumber(N,D)

print("\nO numerador e do denominador simplificados são, respectivamente:\n",q.simplify())
