L = [1, 2]
L3 = 3*L

#1
print("L3 =",L3)

#2

if L3[0]==1:
    print("\nTrue. L3[0] =", L3[0])
else:
    print("False. L3[0] =", L3[0])
    
if L3[-1]==2:
    print("True. L3[-1] =", L3[-1])
else:
    print("False. L3[-1] =", L3[-1])
print("L3[10] returns IndexError: out of range")


#3
L4 = [k**2 for k in L3]
print("\nL4 =",L4)

#L4 squares the elements in L3

#4
L5 = L3 + L4
print("\nL5 =",L5)
