a=frozenset([1,2,3])
b=frozenset([4,3,5,6])

print(a|b)

print(a & b)

print(a-b)

print(a ^ b)

inter=a.intersection(b)
print(inter)

diff=a.difference(b)
print(diff)

un=a.union(b)
print(un)