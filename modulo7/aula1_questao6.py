frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

objetivo_canonica = sorted(palavra_objetivo.lower())

palavras_na_frase = frase.split()

anagramas = []

for palavra in palavras_na_frase:
    palavra_limpa = palavra.strip('.,!?-').lower()
    
    if len(palavra_limpa) == len(palavra_objetivo):
        palavra_canonica = sorted(palavra_limpa)
        
        if palavra_canonica == objetivo_canonica:
            anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
