user_num = int(input("Entre com o numero: "))

par = lambda x: "Par" if x % 2 == 0 else "Impar"

print(f"O numero {user_num} é {par(user_num)}")
