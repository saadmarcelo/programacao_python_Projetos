altura = float(input("Entre com a altura em cm: "))
peso = float(input("Entre com o peso em Kg: "))

IMC = peso / (altura / 100) ** 2

if IMC < 18.5:
    print("MAGREZA")
elif IMC >= 18.5 and IMC < 24.9:
    print("Normal")
elif IMC >= 25.0 and IMC < 29.9:
    print("Sobrepeso")
elif IMC >= 30.0 and IMC < 39.9:
    print("Obesidade")
elif IMC >= 40:
    print("Obesidade grave")
