import random

lista_original = [random.randint(-10, 10) for _ in range(20)]
lista_editada = list(lista_original) 

tamanho = len(lista_editada)
max_negativos = -1
melhor_inicio = -1
melhor_fim = -1

print("Lista Original:", lista_original)

for i in range(tamanho):
    for j in range(i + 1, tamanho + 1):
        intervalo = lista_editada[i:j]
        
        cont_negativos = 0
        for num in intervalo:
            if num < 0:
                cont_negativos += 1
        
        if cont_negativos > max_negativos:
            max_negativos = cont_negativos
            melhor_inicio = i
            melhor_fim = j

if melhor_inicio != -1:
    print(f"\nIntervalo a ser deletado (índices {melhor_inicio} a {melhor_fim-1}) com {max_negativos} negativos.")
    del lista_editada[melhor_inicio:melhor_fim]
else:
    print("\nNenhum número negativo encontrado ou a lista está vazia.")

print("Lista Editada:", lista_editada)
