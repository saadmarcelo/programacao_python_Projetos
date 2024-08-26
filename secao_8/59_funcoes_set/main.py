list1 = set[(1, 2, 3, 4, 5, 6)]
s1 = {1, 2, 4, 5, 6}

s1.add(7)
s1.add(4)  # evita itens duplicados
s1.update([8, 9, 10])  # atualizando uma lista de valores
s1.remove(10)

print(list1)
print(s1)
print(type(list1))
print(type(s1))
