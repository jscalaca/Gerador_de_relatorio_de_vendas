import json
from collections import defaultdict

def carregar_dados(dados='vendas.json'):
 """Carrega os dados para a análise"""
 try:
  with open(dados,"r",encoding="utf-8") as arquivo:
    dados_vendas=json.load(arquivo)
  return dados_vendas
 except FileNotFoundError:
   print(f"arquivo-{dados}-não encontrado")

def total_pedidos(vendas):
   """Retorna o total de pedidos,contando tanto os válidos quanto os cancelados"""
   todos_pedidos=len(vendas)
   return todos_pedidos

def validos(vendas):
   """"Esta funcão só conta os pedidos entregues ou em transporte"""
   pedidos_validos=0
   for item in vendas:
      if item['status'] in ('Entregue','Em transporte'):
       pedidos_validos+=1
   return pedidos_validos

def calcular_faturamento(vendas):
   """Calcula o faturamento total desconsiderando  os pedidos cancelados"""
   faturamento_total=0
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
         faturamento=info['quantidade']* info['valor_unitario']
         faturamento_total+=faturamento
   return faturamento_total

def total_produtos_vendidos(vendas):
   """Calcula o total de unidades vendidas no geral"""
   unidades_vendidas=0
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
        unidades_vendidas+=info['quantidade']
   return unidades_vendidas
def pedidos_por_status(vendas):
    """Calcula quantos pedidos cada status possui"""
    pedidos_por_status=defaultdict(int)
    for item in vendas:
        pedidos_por_status[item['status']]+=1
    return dict(pedidos_por_status)

def quantidade_por_categoria(vendas):
   """Analisa quantos produtos cada categoria possui"""
   unidades_por_categorias=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       unidades_por_categorias[info['categoria']]+=info['quantidade']
   return dict(unidades_por_categorias)

def faturamento_por_categoria(vendas):
   """Calcula o faturamento de cada categoria"""
   faturamento_por_categoria=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       total=info['quantidade']*info['valor_unitario']
       faturamento_por_categoria[info['categoria']]+=total
   return dict(faturamento_por_categoria)

def quantidade_por_produto(vendas):
 """Analisa quantas unidades cada produto vendeu"""
 unidades_por_produto=defaultdict(int)
 for info in vendas:
    if info['status'] in ('Entregue','Em transporte'):
       unidades_por_produto[info['produto']]+=info['quantidade']
 return dict(unidades_por_produto)

def faturamento_por_regiao(vendas):
   """Calcula o faturamento por região"""
   faturamento_por_regiao=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       total=info['quantidade']*info['valor_unitario']
       faturamento_por_regiao[info['regiao']]+=total
   return dict(faturamento_por_regiao)

def cliente_que_mais_gastou(vendas):
   """Analise e compara pra ver qual cliente mais gastou tratando empates"""
   top_cliente=[]
   gastos_clientes=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       total=info['quantidade']*info['valor_unitario']
       gastos_clientes[info['cliente']]+=total
   maior_gasto=max(gastos_clientes.values())
   for item in gastos_clientes.items():
      if item[1]==maior_gasto:
         top_cliente.append([item[0],item[1]])
   return top_cliente

def cliente_que_mais_comprou_unidades(vendas):
   """Analise e compara pra ver qual cliente mais comprou unidades tambem tratando empates """
   top_compras=[]
   compras_clientes=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       compras_clientes[info['cliente']]+=info['quantidade']
   maior_compra=max(compras_clientes.values())
   for item in compras_clientes.items():
      if item[1]==maior_compra:
         top_compras.append([item[0],item[1]])
   return top_compras

def produto_mais_vendido(vendas):
   """Calcula e avalia para listar o produto mais vendido, tambem trata  empates"""
   top_produto=[]
   produtos_vendidos=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       produtos_vendidos[info['produto']]+=info['quantidade']
   top_prod=max(produtos_vendidos.values())
   for item in produtos_vendidos.items():
    if item[1]==top_prod:
       top_produto.append([item[0],item[1]])
   return top_produto

def calcular_ticket_medio(vendas):
   """Calcula o ticket médio"""
   faturamento=calcular_faturamento(vendas)
   pedidos_validos=validos(vendas)
   return f"{faturamento/pedidos_validos:.2f}"

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
