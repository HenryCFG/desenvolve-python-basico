idade_aluno = 15
idade_minima = 18

pode_entrar = idade_aluno >= idade_minima

print("--- Resultado da Comparação ---")
print(f"Valor de pode_entrar (15 >= 18): {pode_entrar}")
print(f"Tipo de pode_entrar: {type(pode_entrar)}")

valor_logico_int = int(pode_entrar)

print("\n--- Conversão para Inteiro ---")
print(f"Valor de pode_entrar convertido para int: {valor_logico_int}")
print(f"Tipo de valor_logico_int: {type(valor_logico_int)}")
