# Projeto: Gerador de Relatório de Vendas

script em Python simples e eficiente pra gerar relatorio de vendas

# Tecnologias Ultilizadas

- Python 3.13.11
- JSON

# Funcionalidades

Importa e lê imformações diretamente do arquivo JSON

# Análises Realizadas:

- Total Pedidos
- Pedidos válidos
- Faturamento total
- Ticket médio
- Pedidos por Status
- Total de Produtos Vendidos
- Quantiade por categoria
- Faturamento por Categoria
- Quantidade por produto
- Produto(s) mais vendido(s)
- Faturamento por Região
- Cliente(s) que mais comprou(aram)
- Clientes que mais gastou(aram)

## Regras de negócios

Pedidos com status "Cancelado" não entram na contagem do faturamento total nem na contagem de total produtos vendidos
Pedidos com status "Entregue" e "Em transporte" entram na contagem de faturamento total e entram na contagem de total de produtos vendidos
