
from collections import  defaultdict
from analises_vendas.pedidos import validos
def total_produtos_vendidos(vendas):
   """Calcula o total de unidades vendidas no geral"""
   unidades_vendidas=0
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
        unidades_vendidas+=info['quantidade']

def quantidade_por_categoria(vendas):
   """Analisa quantos produtos cada categoria possui"""
   unidades_por_categorias=defaultdict(int)
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
       unidades_por_categorias[info['categoria']]+=info['quantidade']
   return dict(unidades_por_categorias)


def calcular_faturamento(vendas):
   """Calcula o faturamento total desconsiderando  os pedidos cancelados"""
   faturamento_total=0
   for info in vendas:
      if info['status'] in ('Entregue','Em transporte'):
         faturamento=info['quantidade']* info['valor_unitario']
         faturamento_total+=faturamento
   return faturamento_total

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