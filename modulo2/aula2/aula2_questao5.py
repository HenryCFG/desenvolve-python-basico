genero = input("Digite seu gênero (M ou F): ").upper()
idade = int(input("Digite sua idade: "))
servico = int(input("Digite seu tempo de serviço (em anos): "))

regra_a_mulher = genero == "F" and idade > 60
regra_a_homem = genero == "M" and idade > 65
regra_a = regra_a_mulher or regra_a_homem

regra_b = servico >= 30

regra_c = idade >= 60 and servico >= 25

pode_aposentar = regra_a or regra_b or regra_c

print(pode_aposentar)
