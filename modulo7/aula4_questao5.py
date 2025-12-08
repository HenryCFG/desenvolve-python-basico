nome_arquivo_csv = "meus_livros.csv"

livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["A Metamorfose", "Franz Kafka", 1915, 104],
    ["Dom Casmurro", "Machado de Assis", 1899, 280],
    ["Sapiens", "Yuval Noah Harari", 2011, 464],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 672],
    ["O Alquimista", "Paulo Coelho", 1988, 208],
]

cabecalho = "Título,Autor,Ano de publicação,Número de páginas\n"

with open(nome_arquivo_csv, 'w', encoding='utf-8') as arquivo_csv:
    arquivo_csv.write(cabecalho)
    
    for livro in livros:
        linha = ",".join(map(str, livro))
        arquivo_csv.write(linha + "\n")

print(f"Arquivo CSV '{nome_arquivo_csv}' criado com sucesso.")
