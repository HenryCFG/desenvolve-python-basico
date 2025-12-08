frase = input("Digite uma frase: ")

vogais_ref = "aeiouáéíóúãõâêîôû"
vogais_encontradas = []
indices = []

for i, letra in enumerate(frase):
    if letra.lower() in vogais_ref:
        vogais_encontradas.append(letra)
        indices.append(i)

print(f"{len(indices)} vogais")
print(f"Índices {indices}")
