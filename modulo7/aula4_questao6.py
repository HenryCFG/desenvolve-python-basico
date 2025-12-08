nome_arquivo_spotify = "spotify-2023.csv"
ANOS_ALVO = range(2012, 2023)

try:
    with open(nome_arquivo_spotify, 'r', encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo_spotify}' não encontrado. Por favor, baixe-o do Kaggle.")
    exit()

print("--- Primeiras 5 linhas do arquivo CSV ---")
for i in range(min(5, len(linhas))):
    print(linhas[i].strip())

musicas_por_ano = {ano: None for ano in ANOS_ALVO}

for i, linha in enumerate(linhas[1:]):
    if linha.count('"') > 0:
        continue

    colunas = linha.strip().split(',')
    
    if len(colunas) < 9:
        continue
        
    try:
        track_name = colunas[0].strip()
        artists_name = colunas[1].strip()
        released_year = int(colunas[3].strip())
        streams = int(colunas[8].strip())
    except ValueError:
        continue

    if released_year in ANOS_ALVO:
        
        dados_musica = [track_name, artists_name, released_year, streams]
        
        ano = released_year
        musica_atual = musicas_por_ano[ano]
        
        if musica_atual is None or streams > musica_atual[3]:
            musicas_por_ano[ano] = dados_musica

lista_musicas_populares = []
for ano in sorted(musicas_por_ano.keys()):
    if musicas_por_ano[ano] is not None:
        lista_musicas_populares.append(musicas_por_ano[ano])

print("\n--- Músicas Mais Populares por Ano (2012 a 2022) ---")
print(lista_musicas_populares)
