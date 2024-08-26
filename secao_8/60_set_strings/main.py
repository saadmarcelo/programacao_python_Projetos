set1 = {"a", "b", "c"}
set2 = {"a", "d", "e"}
set3 = {"c", "d", "f"}

set4 = set1.union(set2)  # soma os 2 sets sem as repeticoes
set5 = set1.difference(
    set2
)  # mostra a diferenca entre o set1 e set2 ( mas apenas em referencia ao set1)
set6 = set1.intersection(set3)  # item q repete nas duas listas
print(set4)
print(set5)
print(set6)
