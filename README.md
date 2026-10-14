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
- Quantidade por categoria
- Faturamento por Categoria
- Quantidade por produto
- Produto(s) mais vendido(s)
- Faturamento por Região
- Cliente(s) que mais comprou(aram)
- Clientes que mais gastou(aram)

## Regras de negócios

Pedidos com status "Cancelado" não entram na contagem do faturamento total nem na contagem de total produtos vendidos
Pedidos com status "Entregue" e "Em transporte" entram na contagem de faturamento total e entram na contagem de total de produtos vendidos

# Atualizações

 Adição de docstrings

Refatorção com funções

Separação da lógica de cad função específica

Os resultados da versão anterior foram mantidos,com código mais organizado e de fácil manutencão

Código modularizado

Separação de responsabilidades

# Core.py

- Carrega os dados

# Clientes.py

- Analisa qual cliente mais gastou e qual comprou o mais unidades

# Pedidos.py

- Analisa o total de pedidos,pedidos validos e pedidos por status

# Produtos.py

- Calcula o faturamento total, quantidade por categoria, faturamento por categoria,faturamento por regiao, ticket medio
- Alem de calcular a quantidade de produtos vendidos, quantidade por produto e produto mais vendido

# main.py

- imprime os resultados das analises
