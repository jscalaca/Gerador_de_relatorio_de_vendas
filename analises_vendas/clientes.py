from collections import defaultdict
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