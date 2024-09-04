def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


user_num = int(input("Entre numero fatorial: "))

print(f"O fatorial de {user_num} é {fatorial(user_num)}")
