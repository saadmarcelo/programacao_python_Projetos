alunos = {
    "nome": "marcelo",
    "idade": 41,
    "materias": ["Fisica", "matematica", "algebra"],
}
for keys, values in alunos.items():
    print(keys, values)

print(alunos.get("materias"))

print(len(alunos))

print(alunos.items())
print(alunos.keys())
print(alunos.values())
