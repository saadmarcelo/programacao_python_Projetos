class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome


usuario1 = Funcionarios("Elena", "Cabral", "01/01/2009")
usuario2 = Funcionarios("Laura", "Saad", "22/05/2020")

print(usuario1.nome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
