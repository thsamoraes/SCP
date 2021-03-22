def half(p,q):
    carry = p and q
    sum0 = int((p or q) and not(p and q))
    return (carry, sum0)

print ("Half adder test (carry, sum):")
print ((0,0)," results in ",half(0,0))
print ((0,1)," results in ",half(0,1))
print ((1,0)," results in ",half(1,0))
print ((1,1)," results in ",half(1,1))


def full(x,y,z):
    carry1 = x and y
    sum1 = int((x or y) and not(x and y))
    carry2 = sum1 and z 
    sum_final = int((sum1 or z) and not(sum1 and z))
    carry_final = carry1 or carry2
    return (carry_final, sum_final)

print ("Full adder test (carry, sum):")
print ((0,0,0)," results in ",full(0,0,0))
print ((0,0,1)," results in ",full(0,0,1))
print ((0,1,0)," results in ",full(0,1,0))
print ((1,0,0)," results in ",full(1,0,0))
print ((0,1,1)," results in ",full(0,1,1))
print ((1,0,1)," results in ",full(1,0,1))
print ((1,1,0)," results in ",full(1,1,0))
print ((1,1,1)," results in ",full(1,1,1))
