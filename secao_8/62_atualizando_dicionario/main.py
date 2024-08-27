alunos = {"nome": "Ana", "idade": 16, "nota_final": "A", "Aprovacao": True}

alunos["nome"] = "José"
print(alunos)

alunos.update({"nome": "Marcelo", "nota_final": "B"})
print(alunos)
alunos.update({"Endereco": "Rua a"})
print(alunos)

print(alunos.get("conta", "Nao existe conta"))

del alunos["idade"]
print(alunos)
