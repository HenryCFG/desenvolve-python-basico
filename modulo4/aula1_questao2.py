n1 = float(input("Leia n1: "))
n2 = float(input("Leia n2: "))
n3 = float(input("Leia n3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")
