fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

celsius_float = (fahrenheit - 32) * (5/9)

celsius_int = int(celsius_float)

print(f"{fahrenheit} graus Fahrenheit são {celsius_int} graus Celsius.")
