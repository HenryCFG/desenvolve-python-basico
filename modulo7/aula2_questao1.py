data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

partes = data_nascimento.split('/')
dia = partes[0]
mes_numero = int(partes[1]) 
ano = partes[2]

nome_mes = meses[mes_numero]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
