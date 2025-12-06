def criar_lista(nome):
    """Função para solicitar e preencher uma lista com o usuário."""
    quantidade = int(input(f"Digite a quantidade de elementos da {nome}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome}:")
    for _ in range(quantidade):
        lista.append(input())
    return lista

lista1 = criar_lista("lista 1")
lista2 = criar_lista("lista 2")

lista_intercalada = []

tamanho_minimo = min(len(lista1), len(lista2))

for i in range(tamanho_minimo):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[tamanho_minimo:])
elif len(lista2) > len(lista1):
    lista_intercalada.extend(lista2[tamanho_minimo:])

print("Lista intercalada:", ' '.join(lista_intercalada))
