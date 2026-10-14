from collections import defaultdict
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

def pedidos_por_status(vendas):
    """Calcula quantos pedidos cada status possui"""
    pedidos_por_status=defaultdict(int)
    for item in vendas:
        pedidos_por_status[item['status']]+=1
    return dict(pedidos_por_status)