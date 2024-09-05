lista = [1, 2, 3, 4, 5, 6]

quadrado = lambda x: x**2

print(list(map(quadrado, lista)))
lista2 = []
for x in lista:
    lista2.append(quadrado(x))


print(list(lista2))
