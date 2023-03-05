string = input("Digite uma string: ")

# Obtém o tamanho da string
tamanho = len(string)

# Converte a string em uma lista de caracteres mutável
lista_caracteres = list(string)

# Inverte a ordem dos caracteres na lista
for i in range(tamanho // 2):
    lista_caracteres[i], lista_caracteres[tamanho - i - 1] = lista_caracteres[tamanho - i - 1], lista_caracteres[i]

# Converte a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

print("String invertida:", string_invertida)