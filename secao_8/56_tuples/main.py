cores_list = ["amarelo", "verde", "azul", "vermelho"]
cores_tuple = ("amarelo", "verde", "azul", "vermelho")

print(type(cores_list))
print(type(cores_tuple))


duas_listas1 = cores_list * 2
duas_listas2 = cores_tuple * 2

print(duas_listas1)
print(duas_listas2)

cores_list.append("Roxo")

print(cores_list)

# cores_tuple.append("Roxo") o tuple nao pode ser modificado
# print(cores_tuple)
