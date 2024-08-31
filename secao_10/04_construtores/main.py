class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


usuario1 = Funcionarios("Elena", "Cabral", "01/01/2009")
usuario2 = Funcionarios("Laura", "Saad", "22/05/2020")

print(usuario1.nome)
print(usuario2.data_nascimento)
