a = []
a = [1, 2, 3]
a.append(4)
print(a)

a.insert(1, 5)
print(a)

a.remove(2)
print(a)

ultimo_elemento = a.pop()
print(ultimo_elemento)
print(a)
del a[0]
print(a)