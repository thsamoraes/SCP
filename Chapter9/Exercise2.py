from itertools import islice

def sequence(u0):
    yield u0
    while True:
        u0 = 2*u0
        yield u0
        
print(list(islice(sequence(1), 20)))
