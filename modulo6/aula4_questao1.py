pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares [20-50]:", pares)

quadrados = [x**2 for x in range(1, 10)]
print("Quadrados de [1-9]:", quadrados)

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7 [1-100]:", divisiveis_por_7)

paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print("Paridade do range(0, 30, 3):", paridade)
