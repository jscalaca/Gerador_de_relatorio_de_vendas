# Projeto: Gerador de Relatório de Vendas
script em Python simples e eficiente pra gerar relatorio de vendas
# Tecnologias Ultilizadas 
- Python 3.13.11
- JSON
# Funcionalidades
Importa e lê imformações diretamente do arquivo JSON
# Análises Realizadas:
- Total Pedidos
- Faturamento Total
- Pedidos por Status
- Total de Produtos Vendidos
# Regras de Negocio
Pedidos com status "Cancelado" não entram na contagem do faturamento total nem na contagem de total produtos vendidos
Pedidos com status "Entregue" e "Em transporte" entram na contagem de faturamento total e entram na contagem de total de produtos vendidos


