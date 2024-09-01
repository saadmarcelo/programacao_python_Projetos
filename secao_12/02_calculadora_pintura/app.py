rendimento = int(input("Entre com o rendimento da tinta: "))
altura = int(input("Entre com a altura da parade: "))
largura = int(input("Entre com a largura da parede: "))


def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f"Voce precisa de {total} latas de tinta")


calculo_tinta()
