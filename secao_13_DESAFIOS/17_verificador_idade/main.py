idade = int(input("Entre com a idade: "))

if idade < 13:
    print("Voce é uma criança")
elif 13 <= idade <= 19:
    print("Voce é um adolecente")
else:
    print("Voce é um adulto")
