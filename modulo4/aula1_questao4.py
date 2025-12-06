n = int(input("Digite quantos números serão lidos (n): "))

maior = 0

while n > 0:
    x = int(input("Digite um número (x): "))
    
    if x > maior:
        maior = x
        
    n = n - 1

print("O maior número lido foi:")
print(maior)
