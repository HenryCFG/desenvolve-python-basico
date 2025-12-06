import random
import math

n = int(input("Digite o valor de n (quantidade de números aleatórios): "))
soma = 0

for i in range(n):
    valor_aleatorio = random.randint(0, 100)
    soma = soma + valor_aleatorio
    print(f"Valor {i+1} gerado: {valor_aleatorio}")

raiz_quadrada = math.sqrt(soma)

print(f"A soma dos {n} valores é: {soma}")
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}")
