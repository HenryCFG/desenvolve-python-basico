def validador_senha(senha):
    if len(senha) < 8:
        return False
        
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    caracteres_especiais = "@#$%^&+=!"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_especial = True
            
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(f"'{senha1}': {validador_senha(senha1)}")
print(f"'{senha2}': {validador_senha(senha2)}")
print(f"'{senha3}': {validador_senha(senha3)}")
