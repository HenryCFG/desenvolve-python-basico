import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_cript = []
    
    MIN_CHAR = 33
    MAX_CHAR = 126
    RANGE = MAX_CHAR - MIN_CHAR + 1

    for nome in nomes:
        nome_criptografado = ""
        for char in nome:
            char_ord = ord(char)
            
            if MIN_CHAR <= char_ord <= MAX_CHAR:
                char_cript_ord = (char_ord - MIN_CHAR + chave) % RANGE + MIN_CHAR
                char_cript = chr(char_cript_ord)
            else:
                char_cript = char

            nome_criptografado += char_cript
        
        nomes_cript.append(nome_criptografado)
        
    return nomes_cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_gerada = encrypt(nomes)

print(f"Chave de criptografia gerada: {chave_gerada}")
print(f"Nomes originais: {nomes}")
print(f"Nomes criptografados: {nomes_criptografados}")
