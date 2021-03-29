L={1,2,3,2,3,6,5,4,8}
M={'a','k','hello',50,8}
N={-2,4,7,6,8,9,20}
O={123456321,0}

print(set([]).issubset(L))
print(set([]).issubset(M))
print(set([]).issubset(N))
print(set([]).issubset(O))
print(set([]).issubset(O.union(L)))
print(set([]).issubset(O.union(L.union(M))))
print(set([]).issubset(O.union(L.union(M.intersection(N)))))
