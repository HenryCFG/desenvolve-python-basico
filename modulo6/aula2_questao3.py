import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)

interseccao = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)

interseccao_ordenada = sorted(interseccao)
print("\nA lista intersecção ordenada:", interseccao_ordenada)

print("\nContagem:")
for elemento in interseccao_ordenada:
    cont_l1 = lista1.count(elemento)
    cont_l2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={cont_l1}, lista2={cont_l2})")
