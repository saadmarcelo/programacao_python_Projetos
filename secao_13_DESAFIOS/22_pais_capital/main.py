x = {
    "brasil": "brasilia",
    "argentina": "buenos aires",
    "franca": "paris",
    "inglaterra": "londres",
}

pesquisa_capital = input("Entre com o nome do pais que deseja pesquisar: ")

if pesquisa_capital in x:
    print(f"A capital de {pesquisa_capital} é {x[pesquisa_capital]} ")
else:
    print(f"A capital {pesquisa_capital} não esta na lista")
