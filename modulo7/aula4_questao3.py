import re

nome_arquivo = "estomago.txt"

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado. Por favor, baixe o arquivo e salve-o no diretório.")
    exit()

print("--- Primeiras 25 Linhas ---")
for i, linha in enumerate(linhas[:25]):
    print(linha.strip()) 

num_linhas = len(linhas)
print("\n--- Estatísticas ---")
print(f"Número total de linhas: {num_linhas}")

linha_mais_longa = max(linhas, key=len)
print(f"Linha com maior número de caracteres ({len(linha_mais_longa.strip())}):")
print(linha_mais_longa.strip())

padrao_nonato = re.compile(r'\bnonato\b', re.IGNORECASE)
padrao_iria = re.compile(r'\bíria\b', re.IGNORECASE)

cont_nonato = 0
cont_iria = 0
texto_completo = "".join(linhas) 

cont_nonato = len(padrao_nonato.findall(texto_completo))
cont_iria = len(padrao_iria.findall(texto_completo))

print(f"Menções a 'Nonato': {cont_nonato}")
print(f"Menções a 'Íria': {cont_iria}")
