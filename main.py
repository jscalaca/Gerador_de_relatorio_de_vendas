from analises_vendas.core import carregar_dados
from analises_vendas.pedidos import(total_pedidos,validos,pedidos_por_status)
from analises_vendas.produtos import(faturamento_por_categoria,calcular_faturamento,faturamento_por_regiao,produto_mais_vendido,total_produtos_vendidos,quantidade_por_categoria,quantidade_por_produto,calcular_ticket_medio)
from analises_vendas.clientes import (cliente_que_mais_comprou_unidades,cliente_que_mais_gastou)

def imprimir_relatorio(vendas):

  print('==='*4,'RELATÓRIO DE VENDAS','==='*4)
  print('---'*10)
  print(f"Total de pedidos: {total_pedidos(vendas)} unidades")
  print('---'*10)
  print(f'Pedidos válidos: {validos(vendas)} ')
  print('---'*10)
  print(f'Faturamento total: {calcular_faturamento(vendas)} R$')
  print('---'*10)
  print(f'Total de produtos vendidos: {total_produtos_vendidos(vendas)} unidades')
  print('---'*10)
  print('Total de pedidos por status:')
  for item in pedidos_por_status(vendas).items():
    print(f'-{item[0]}: {item[1]} pedidos')
  print('---'*10)
  print('Quantidade por categoria:')
  for item in quantidade_por_categoria(vendas).items():
    print(f'-{item[0]}: {item[1]} unidades')
  print('---'*10)
  print('Faturamento por categoria:')
  for info in faturamento_por_categoria(vendas).items():
    print(f'-{info[0]}: {info[1]} R$')
  print('---'*10)
  print(f'Quantidade por produto:')
  for info in quantidade_por_produto(vendas).items():
    print(f'-{info[0]}: {info[1]} unidades')
  print('---'*10)
  print('Faturamento por região:')
  for item in faturamento_por_regiao(vendas).items():
    print(f'-{item[0]}: {item[1]} R$')
  print('---'*10)
  print('Cliente(s)  que mais gastou(aram):')
  for item in cliente_que_mais_gastou(vendas):
    print(f'-{item[0]}: {item[1]} R$ ')
  print('---'*10)
  print('Cliente(s) que mais comprou(aram):')
  for item in cliente_que_mais_comprou_unidades(vendas):
    print(f'-{item[0]}: {item[1]} unidades')
  print('---'*10)
  print('Produto mais  vendido:')
  for item in produto_mais_vendido(vendas):
    print(f'-{item[0]}: {item[1]} unidades')
  print('---'*10)
  print(f'Ticket médio: {calcular_ticket_medio(vendas)} R$')

dados_vendas=carregar_dados()

imprimir_relatorio(dados_vendas)
