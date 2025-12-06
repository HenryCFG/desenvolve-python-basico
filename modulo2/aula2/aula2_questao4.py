classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

regra_guerreiro = (forca >= 15) and (magia <= 10)
regra_mago = (forca <= 10) and (magia >= 15)
regra_arqueiro = (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15)

consistente = (classe == "guerreiro" and regra_guerreiro) or \
              (classe == "mago" and regra_mago) or \
              (classe == "arqueiro" and regra_arqueiro)

print(f"Pontos de atributo consistentes com a classe escolhida: {consistente}")
