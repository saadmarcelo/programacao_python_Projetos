try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar o numero em numero")
else:
    print("O usuario digitou um valor correto")
    resultado = valor * 2
    print(resultado)

print("Mais codigo abaixo ")
