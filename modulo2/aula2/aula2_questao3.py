idade = int(input("Digite sua idade: "))
jogou_str = input("Já jogou pelo menos 3 jogos de tabuleiro? ")
vitorias = int(input("Quantos jogos já venceu? "))

jogou_3_jogos = jogou_str == "True"

criterio_idade = idade >= 16 and idade <= 18
criterio_jogos = jogou_3_jogos
criterio_vitorias = vitorias >= 1

apto = criterio_idade and criterio_jogos and criterio_vitorias

print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
