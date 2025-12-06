n = int(input("Digite a quantidade de respondentes (N): "))

soma_idades = 0
contador = 0

while contador < n:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades = soma_idades + idade
    contador = contador + 1

if n > 0:
    media = soma_idades / n
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhum respondente foi registrado.")
