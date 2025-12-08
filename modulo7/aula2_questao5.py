import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase_palavras = []
    
    for palavra in palavras:
        tamanho = len(palavra)
        
        if tamanho <= 2:
            nova_frase_palavras.append(palavra)
            continue
            
        primeiro = palavra[0]
        ultimo = palavra[-1]
        
        meio = list(palavra[1:-1])
        
        random.shuffle(meio)
        
        palavra_embaralhada = primeiro + "".join(meio) + ultimo
        nova_frase_palavras.append(palavra_embaralhada)
        
    return " ".join(nova_frase_palavras)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(f"Frase original: {frase}")
print(f"Frase embaralhada: {resultado}")
