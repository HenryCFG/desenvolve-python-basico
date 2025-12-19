# Trabalho Prático - TechFlow Solutions

## Introdução
Este sistema gerencia a **TechFlow Solutions**, uma loja de hardware. 
- **Usuários:** Gerente (total) e Funcionário (estoque).
- **Produtos:** Peças de computador com ID, Nome, Preço e Quantidade.

## Implementação
- **Estruturas:** - Usuários: Dicionário para busca rápida.
  - Produtos: Lista de dicionários para facilitar ordenação.
- **Arquivos:** Formato `.txt` com campos separados por vírgula.
- **CRUD:** - `cadastrar_produto` (C)
  - `listar_produtos` (R)
  - `atualizar_estoque` (U)
  - `excluir_produto` (D)

## Conclusão
O maior desafio foi a conversão de tipos ao ler os arquivos. A escolha de usar listas com dicionários internos permitiu o uso eficiente da função `sorted()` com `lambda`.
