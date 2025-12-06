comprimento = int(input("Digite o comprimento do terreno (m): "))
largura = int(input("Digite a largura do terreno (m): "))
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
