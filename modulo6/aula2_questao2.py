import random

num_elementos = random.randint(5, 20)

elementos = []
for _ in range(num_elementos):
    elementos.append(random.randint(1, 10))

print("Número de elementos gerados:", num_elementos)
print("A lista elementos:", elementos)

soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos

print("A soma dos valores da lista:", soma_valores)
print(f"A média dos valores da lista: {media_valores:.2f}")
