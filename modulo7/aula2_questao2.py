frase = input("Digite uma frase: ")

vogais = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕ"

frase_modificada = frase

for vogal in vogais:
    frase_modificada = frase_modificada.replace(vogal, '*')

print(f"Frase modificada: {frase_modificada}")
