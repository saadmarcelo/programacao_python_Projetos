def dobro(num):
    return num * 2


def quadrado(num):
    return dobro(num) ** 2


user_num = int(input("Entre com o numero: "))

print(quadrado(user_num))
