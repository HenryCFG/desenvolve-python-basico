# Relatório Técnico: Gerenciador TechFlow Solutions

## 1. Introdução
A empresa modelada é a **TechFlow Solutions**, uma varejista de hardware. O software visa gerenciar o estoque de produtos e controlar o acesso de diferentes perfis de funcionários.
- **Usuários:** Gerente (Admin) e Funcionário (Operacional).
- **Produtos:** Peças de hardware (SSDs, Mouses, etc) com preço e quantidade.

## 2. Implementação

### 2.1 Usuários

- **Estrutura de Dados:** Dicionário de Dicionários. Permite acesso direto aos dados do usuário pelo nome (Chave).
- **Registro em Arquivo:** `usuarios.txt` armazena dados separados por vírgula. Ex: `admin,123,gerente`.
- **Funcionalidades CRUD:**
  - (R) Login e validação de nível.
  - (R) Verificação de permissão no menu.

### 2.2 Produtos
- **Estrutura de Dados:** Lista de Dicionários. Cada dicionário é um objeto "Produto". Escolhida para facilitar a ordenação por diferentes critérios (nome e preço).
- **Registro em Arquivo:** `produtos.txt` usa o formato CSV simples.
- **Funcionalidades CRUD:**
  - (C) `cadastrar_produto`: Adiciona novos itens.
  - (R) `listar_produtos`: Exibe registros ordenados (Exigência: Nome/Preço).
  - (R) `buscar_produto`: Recupera um registro específico.
  - (U) `atualizar_produto`: Edita a quantidade em estoque.
  - (D) `excluir_produto`: Remove registros do sistema.

## 3. Conclusão
O sistema cumpre todos os requisitos, utilizando estruturas condicionais, de repetição e funções comentadas. A maior dificuldade foi o tratamento de strings vindo dos arquivos para garantir que a ordenação numérica (preço) não seguisse a ordem alfabética.
