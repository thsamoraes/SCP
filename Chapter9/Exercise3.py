from itertools import islice

def even_numbers(u0):
    yield u0
    while True:
        u0 = u0+2
        yield u0
        
print(list(islice(even_numbers(0), 501)))
