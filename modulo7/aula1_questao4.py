numero = input("Digite o número: ")

numero_limpo = numero.replace('-', '').replace('.', '')

if len(numero_limpo) == 8:
    numero_formatado = "9" + numero_limpo
elif len(numero_limpo) == 9:
    if numero_limpo[0] != '9':
        numero_formatado = "9" + numero_limpo
    else:
        numero_formatado = numero_limpo
else:
    print("Número inválido. O celular deve ter 8 ou 9 dígitos.")
    exit()

formatado_final = f"{numero_formatado[:5]}-{numero_formatado[5:]}"

print(f"Número completo: {formatado_final}")
