import string

nome_arquivo_entrada = "frase.txt"
nome_arquivo_saida = "palavras.txt"

try:
    with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado. Execute o exercício 1 primeiro.")
    exit()

for pontuacao in string.punctuation:
    conteudo = conteudo.replace(pontuacao, '')

palavras = [palavra for palavra in conteudo.split() if palavra.strip()]

with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

print("\nConteúdo do arquivo 'palavras.txt':")
with open(nome_arquivo_saida, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
