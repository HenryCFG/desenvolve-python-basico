nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))
total1 = preco1 * quantidade1

nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))
total2 = preco2 * quantidade2

nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))
total3 = preco3 * quantidade3

preco_total_final = total1 + total2 + total3

print(f"Total: R${preco_total_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
