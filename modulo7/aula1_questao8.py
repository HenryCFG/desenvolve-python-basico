def calcula_digito_verificador(cpf_base):
    """Calcula um único dígito verificador para o CPF."""
    
    tamanho = len(cpf_base)
    multiplicador_inicial = tamanho + 1
    soma = 0
    
    for i in range(tamanho):
        digito = int(cpf_base[i])
        multiplicador = multiplicador_inicial - i
        soma += digito * multiplicador
        
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def valida_cpf(cpf):
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    
    if len(cpf_limpo) != 11:
        return False
        
    if len(set(cpf_limpo)) == 1:
        return False

    digitos_base = cpf_limpo[:9]
    dv1_fornecido = int(cpf_limpo[9])
    dv2_fornecido = int(cpf_limpo[10])

    dv1_calculado = calcula_digito_verificador(digitos_base)
    
    if dv1_calculado != dv1_fornecido:
        return False

    digitos_base_dv2 = digitos_base + str(dv1_calculado)
    dv2_calculado = calcula_digito_verificador(digitos_base_dv2)

    if dv2_calculado != dv2_fornecido:
        return False
        
    return True

cpf_entrada = input("Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string): ")

if valida_cpf(cpf_entrada):
    print("Válido")
else:
    print("Inválido")
