num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

diferenca_bruta = num1 - num2
diferenca_absoluta = abs(diferenca_bruta)
resultado_arredondado = round(diferenca_absoluta, 2)

print(f"A diferença absoluta entre os números é: {resultado_arredondado}")
