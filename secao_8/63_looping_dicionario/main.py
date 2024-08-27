alunos = {"nome": "Ana", "idade": 16, "nota_final": "A", "Aprovacao": True}


for x in alunos.keys():
    print(x)

for x in alunos.values():
    print(x)

for x in alunos.items():
    print(x)

for keys, values in alunos.items():
    print(keys, values)
