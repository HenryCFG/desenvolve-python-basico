import os

# --- PERSISTÊNCIA DE DADOS ---

def carregar_usuarios():
    """Lê o arquivo de usuários e retorna um dicionário."""
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

def salvar_usuarios(usuarios):
    """Salva o dicionário de usuários no arquivo txt."""
    with open("usuarios.txt", "w", encoding="utf-8") as f:
        for nome, dados in usuarios.items():
            f.write(f"{nome},{dados['senha']},{dados['nivel']}\n")

def carregar_produtos():
    """Lê o arquivo de produtos e retorna uma lista de dicionários."""
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
    """Salva a lista de produtos no arquivo txt."""
    with open("produtos.txt", "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p['id']},{p['nome']},{p['preco']},{p['qtd']}\n")

# --- CRUD PRODUTOS ---

def listar_produtos(produtos, criterio="nome"):
    """R - Read: Lista produtos ordenados."""
    if not produtos:
        print("\nEstoque vazio.")
        return
    chave = "nome" if criterio == "nome" else "preco"
    ordenados = sorted(produtos, key=lambda x: x[chave])
    print(f"\n--- LISTA DE PRODUTOS (ORDEM: {criterio.upper()}) ---")
    for p in ordenados:
        print(f"ID: {p['id']} | {p['nome']} | R${p['preco']:.2f} | Qtd: {p['qtd']}")

def buscar_produto(produtos):
    """R - Read: Busca por nome."""
    busca = input("Digite o nome para buscar: ").lower()
    for p in produtos:
        if busca in p['nome'].lower():
            print(f"Achado -> ID: {p['id']} | {p['nome']} | R${p['preco']}")
            return
    print("Produto não encontrado.")

def cadastrar_produto(produtos):
    """C - Create: Adiciona novo produto."""
    id_p = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    qtd = int(input("Qtd inicial: "))
    produtos.append({"id": id_p, "nome": nome, "preco": preco, "qtd": qtd})
    salvar_produtos(produtos)
    print("Sucesso!")

def atualizar_estoque(produtos):
    """U - Update: Altera quantidade."""
    id_p = input("ID do produto: ")
    for p in produtos:
        if p['id'] == id_p:
            p['qtd'] = int(input(f"Nova quantidade para {p['nome']}: "))
            salvar_produtos(produtos)
            print("Atualizado!")
            return
    print("ID inválido.")

def excluir_produto(produtos):
    """D - Delete: Remove do sistema."""
    id_p = input("ID para remover: ")
    for i, p in enumerate(produtos):
        if p['id'] == id_p:
            produtos.pop(i)
            salvar_produtos(produtos)
            print("Removido!")
            return
    print("ID inválido.")

# --- LOGIN E MENU ---

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()
    
    print("SISTEMA TECHFLOW SOLUTIONS")
    user = input("User: ")
    senha = input("Senha: ")

    if user in usuarios and usuarios[user]["senha"] == senha:
        nivel = usuarios[user]["nivel"]
        while True:
            print(f"\nMENU - ACESSO: {nivel.upper()}")
            print("1. Listar (Nome)\n2. Listar (Preço)\n3. Buscar")
            if nivel == "gerente":
                print("4. Cadastrar\n5. Atualizar\n6. Excluir")
            elif nivel == "funcionario":
                print("4. Atualizar Estoque")
            print("0. Sair")
            
            op = input("Opção: ")
            if op == "1": listar_produtos(produtos, "nome")
            elif op == "2": listar_produtos(produtos, "preco")
            elif op == "3": buscar_produto(produtos)
            elif op == "4":
                if nivel == "gerente": cadastrar_produto(produtos)
                else: atualizar_estoque(produtos)
            elif op == "5" and nivel == "gerente": atualizar_estoque(produtos)
            elif op == "6" and nivel == "gerente": excluir_produto(produtos)
            elif op == "0": break
    else: print("Erro de login.")

if __name__ == "__main__":
    main()