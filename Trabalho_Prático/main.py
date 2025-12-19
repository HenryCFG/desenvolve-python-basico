import os

# --- GERÊNCIA DE ARQUIVOS ---

def carregar_usuarios():
    """
    Lê o arquivo 'usuarios.txt' e carrega os dados em um dicionário.
    Saída: Dicionário com estrutura {nome: {senha, nivel}}.
    """
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(',')
                    if len(partes) == 3:
                        nome, senha, nivel = partes
                        usuarios[nome] = {"senha": senha, "nivel": nivel}
    return usuarios

def carregar_produtos():
    """
    Lê o arquivo 'produtos.txt' e carrega em uma lista de dicionários.
    Saída: Lista de dicionários contendo id, nome, preco (float) e qtd (int).
    """
    produtos = []
    if os.path.exists("produtos.txt"):
        with open("produtos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(',')
                    if len(partes) == 4:
                        id_p, nome, preco, qtd = partes
                        produtos.append({
                            "id": id_p, "nome": nome, 
                            "preco": float(preco), "qtd": int(qtd)
                        })
    return produtos

def salvar_produtos(produtos):
    """
    Recebe a lista de produtos e sobrescreve o arquivo 'produtos.txt'.
    Entrada: lista_produtos (list).
    """
    with open("produtos.txt", "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p['id']},{p['nome']},{p['preco']},{p['qtd']}\n")

# --- CRUD DE PRODUTOS ---

def cadastrar_produto(produtos):
    """
    C do CRUD: Adiciona um novo produto à lista e salva no arquivo.
    Entrada: lista_produtos (list).
    """
    print("\n--- Cadastro de Produto ---")
    id_p = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    produtos.append({"id": id_p, "nome": nome, "preco": preco, "qtd": qtd})
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

def listar_produtos(produtos, criterio="nome"):
    """
    R do CRUD: Exibe os registros ordenados por nome ou preço.
    Entrada: lista_produtos (list), criterio (str).
    """
    if not produtos:
        print("\nNão há produtos cadastrados.")
        return
    
    # Ordenação usando o conceito de Strings e Chaves
    chave = "nome" if criterio == "nome" else "preco"
    ordenados = sorted(produtos, key=lambda x: x[chave])
    
    print(f"\n--- Produtos Ordenados por {criterio.upper()} ---")
    for p in ordenados:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['qtd']}")

def buscar_produto(produtos):
    """
    R do CRUD: Busca um produto específico pelo nome (String).
    Entrada: lista_produtos (list).
    """
    busca = input("\nDigite o nome para buscar: ").lower()
    for p in produtos:
        if busca in p['nome'].lower():
            print(f"Resultado: ID {p['id']} - {p['nome']} - R${p['preco']}")
            return
    print("Produto não encontrado.")

def atualizar_produto(produtos):
    """
    U do CRUD: Atualiza a quantidade em estoque de um produto existente.
    Entrada: lista_produtos (list).
    """
    id_p = input("\nID do produto para atualizar: ")
    for p in produtos:
        if p['id'] == id_p:
            p['qtd'] = int(input(f"Novo estoque para {p['nome']}: "))
            salvar_produtos(produtos)
            print("Estoque atualizado!")
            return
    print("ID não encontrado.")

def excluir_produto(produtos):
    """
    D do CRUD: Remove um produto da lista e do arquivo.
    Entrada: lista_produtos (list).
    """
    id_p = input("\nID do produto para excluir: ")
    for i, p in enumerate(produtos):
        if p['id'] == id_p:
            confirmar = input(f"Tem certeza que deseja excluir {p['nome']}? (s/n): ")
            if confirmar.lower() == 's':
                produtos.pop(i)
                salvar_produtos(produtos)
                print("Produto removido.")
            return
    print("ID não encontrado.")

# --- FLUXO PRINCIPAL ---

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()
    
    print("="*30)
    print(" SISTEMA TECHFLOW SOLUTIONS ")
    print("="*30)
    
    user = input("Usuário: ")
    senha = input("Senha: ")

    if user in usuarios and usuarios[user]["senha"] == senha:
        nivel = usuarios[user]["nivel"]
        print(f"\nLogin bem-sucedido! Bem-vindo(a), {user} ({nivel})")
        
        while True:
            print("\n" + "-"*20)
            print(f"MENU PRINCIPAL")
            print("1. Listar por Nome\n2. Listar por Preço\n3. Buscar Produto")
            
            # Controle de Níveis de Permissão
            if nivel == "gerente":
                print("4. Cadastrar Novo Produto\n5. Atualizar Estoque\n6. Excluir Produto")
            else:
                print("4. Atualizar Estoque (Permissão limitada)")
                
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1": listar_produtos(produtos, "nome")
            elif opcao == "2": listar_produtos(produtos, "preco")
            elif opcao == "3": buscar_produto(produtos)
            elif opcao == "4":
                if nivel == "gerente": cadastrar_produto(produtos)
                else: atualizar_produto(produtos)
            elif opcao == "5" and nivel == "gerente": atualizar_produto(produtos)
            elif opcao == "6" and nivel == "gerente": excluir_produto(produtos)
            elif opcao == "0": break
            else: print("Opção inválida ou acesso negado.")
    else:
        print("\nUsuário ou senha incorretos.")

if __name__ == "__main__":
    main()