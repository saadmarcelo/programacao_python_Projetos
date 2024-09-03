cidades = ("manaus", "recife", "fortaleza")

pesquisa_cidade = input("Entre com a cidade: ")

if pesquisa_cidade in cidades:
    print(f"A cidade {pesquisa_cidade} esta na lista")
else:
    print(f"A cidade {pesquisa_cidade} nao esta na lista")
