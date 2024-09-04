def potencia(base, exp=2):
    return base**exp


user_base = int(input("Entre com o numero da base: "))
user_expoente = input("Entre com o numero da expoente (default 2): ")
if user_expoente:
    print(f"O resultado é: {potencia(user_base, int(user_expoente))}")
else:
    print(f"O resultado é: {potencia(user_base)}")
