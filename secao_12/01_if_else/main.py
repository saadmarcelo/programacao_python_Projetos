temperatura = int(input("Entre com a temperadura da carne: "))

if temperatura < 48:
    ponto_carne = "Cozinhe a carne pro mais alguns minutos"
elif 54 > temperatura >= 48:
    ponto_carne = "carne Rare"
elif 60 > temperatura >= 54:
    ponto_carne = "carne medium rare"
elif 65 > temperatura >= 60:
    ponto_carne = "carne medium"
elif 71 > temperatura >= 65:
    ponto_carne = "carne medium well"
elif temperatura >= 71:
    ponto_carne = "carne well done"

print("a carne esta com a temperatura de %d e esta %s" % (temperatura, ponto_carne))
