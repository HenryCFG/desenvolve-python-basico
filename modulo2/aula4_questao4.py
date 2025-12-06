quantia = int(input("Digite a quantia em reais: "))

notas = [100, 50, 20, 10, 5, 2, 1]

print(f"Quantia de entrada: {quantia}")

nota_100 = quantia // 100
quantia = quantia % 100
print(f"{nota_100} nota(s) de R$100,00")

nota_50 = quantia // 50
quantia = quantia % 50
print(f"{nota_50} nota(s) de R$50,00")

nota_20 = quantia // 20
quantia = quantia % 20
print(f"{nota_20} nota(s) de R$20,00")

nota_10 = quantia // 10
quantia = quantia % 10
print(f"{nota_10} nota(s) de R$10,00")

nota_5 = quantia // 5
quantia = quantia % 5
print(f"{nota_5} nota(s) de R$5,00")

nota_2 = quantia // 2
quantia = quantia % 2
print(f"{nota_2} nota(s) de R$2,00")

nota_1 = quantia // 1
quantia = quantia % 1
print(f"{nota_1} nota(s) de R$1,00")
