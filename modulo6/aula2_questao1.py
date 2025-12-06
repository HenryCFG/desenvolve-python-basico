import random

lista_original = []
for _ in range(20):
    lista_original.append(random.randint(-100, 100))

lista_ordenada = sorted(lista_original)
print("Lista Ordenada (sem modificar a original):", lista_ordenada)

print("Lista Original:", lista_original)

maior_valor = max(lista_original)
indice_maior = lista_original.index(maior_valor)
print("Maior valor:", maior_valor)
print("Índice do maior valor:", indice_maior)

menor_valor = min(lista_original)
indice_menor = lista_original.index(menor_valor)
print("Menor valor:", menor_valor)
print("Índice do menor valor:", indice_menor)
