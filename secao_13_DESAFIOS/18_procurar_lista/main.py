carros = ["BMW X6", "BMW i5", "BMW i8"]

nome_carro = input("Entre com o carro que deseja comprar: ")

if nome_carro in carros:
    print(f"o Carro {nome_carro} esta disponivel em estoque")
else:
    print(f"Desculpe o {nome_carro} nao esta disponivel")
