nome = input("Digite seu nome: ")
tamanho = len(nome)

for i in range(tamanho):
    print(nome[:i+1])
