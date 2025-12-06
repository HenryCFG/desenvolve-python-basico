lista_original = []
print("Digite números inteiros (digite qualquer letra para finalizar):")

while True:
    try:
        num = int(input())
        lista_original.append(num)
    except ValueError:
        if len(lista_original) < 4:
            print("Por favor, insira pelo menos 4 valores.")
            continue
        break

print("\n--- Resultados do Fatiamento ---")

print("Lista original:", lista_original)

print("3 primeiros elementos:", lista_original[0:3])

print("2 últimos elementos:", lista_original[-2:])

print("Lista invertida:", lista_original[::-1])

print("Elementos de índice par:", lista_original[::2])

print("Elementos de índice ímpar:", lista_original[1::2])
