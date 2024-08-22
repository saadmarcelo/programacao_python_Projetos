def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num

    return resultado


X = soma(2, 3, 4, 5)
print(X)
