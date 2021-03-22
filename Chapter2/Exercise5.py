def implication(A,B):
    if A == False or A == B == True:
        return True

    else:
        return False
    
print("C is {0}".format(implication(False, True)))

print("C is {0}".format(implication(False, False)))

print("C is {0}".format(implication(True, True)))

print("C is {0}".format(implication(True, False)))
