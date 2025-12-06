distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

valor_por_kg = 0.0

if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

valor_frete = valor_por_kg * peso

if peso > 10:
    valor_frete = valor_frete + 10.00
    
print(f"O valor do frete é de R${valor_frete:.2f}")
