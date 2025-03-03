A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print(len(A | B))
print(len(B - (A | C)))

print(C - (A | B))
print(A & C)
print(B & C)
print(A & C - B)
print(A & B & C)
print(B - (A | C))
