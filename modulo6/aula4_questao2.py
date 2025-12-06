frase = input("Digite uma frase: ")
vogais_ref = 'aeiouáéíóúãõâêîôû'

vogais = [char for char in frase if char.lower() in vogais_ref and char != ' ']
vogais_ordenadas = sorted(vogais)

consoantes = [char for char in frase if char.lower() not in vogais_ref and char != ' ']

print(f"Vogais: {vogais_ordenadas}")
print(f"Consoantes: {consoantes}")
