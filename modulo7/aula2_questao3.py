import string

def verifica_palindromo(frase):
    frase_normalizada = frase.lower()
    
    caracteres_invalidos = string.whitespace + string.punctuation
    
    frase_limpa = ""
    for char in frase_normalizada:
        if char not in caracteres_invalidos:
            frase_limpa += char
            
    return frase_limpa == frase_limpa[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if entrada.lower() == "fim":
        break
        
    if verifica_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')
