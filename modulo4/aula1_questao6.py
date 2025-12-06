n = int(input())

total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0
contador = 0

while contador < n:
    entrada = input().split()
    
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    total_cobaias = total_cobaias + quantia

    if tipo == 'S':
        total_sapos = total_sapos + quantia
    elif tipo == 'R':
        total_ratos = total_ratos + quantia
    elif tipo == 'C':
        total_coelhos = total_coelhos + quantia

    contador = contador + 1

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")

if total_cobaias > 0:
    perc_coelhos = (total_coelhos / total_cobaias) * 100
    perc_ratos = (total_ratos / total_cobaias) * 100
    perc_sapos = (total_sapos / total_cobaias) * 100
    
    print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
    print(f"Percentual de ratos: {perc_ratos:.2f} %")
    print(f"Percentual de sapos: {perc_sapos:.2f} %")
else:
    print("Nenhum cálculo de percentual é possível, pois não houve cobaias.")
