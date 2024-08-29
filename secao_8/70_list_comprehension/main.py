frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]
# frutas2 = []
# for iten in frutas1:
#    if "a" in iten:
#        frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if "n" in iten]
print(frutas2)
