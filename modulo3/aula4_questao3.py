ano = int(input("Insira um ano para verificar se é bissexto: "))

regra1 = (ano % 4 == 0) and (ano % 100 != 0)

regra2 = (ano % 400 == 0)

bissexto = regra1 or regra2

if bissexto:
    print("Bissexto")
else:
    print("Não Bissexto")
