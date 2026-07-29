import json
from collections import defaultdict
with open("vendas.json","r",encoding="utf-8") as arquivo:
    dados_vendas=json.load(arquivo)
total_pedidos=len(dados_vendas)
faturamento_total=0
produtos_vendidos=0
pedidos_validos=0
pedido_por_status=defaultdict(int)
unidades_por_categorias=defaultdict(int)
total_por_categoria=defaultdict(int)
cliente_compras=defaultdict(int)
cliente_gastos=defaultdict(int)
unidades_produtos=defaultdict(int)
total_por_regiao=defaultdict(int)
for item in dados_vendas:
 if item['status'] in("Entregue","Em transporte"):
    valor=item['quantidade']*item['valor_unitario']
    faturamento_total+=valor
    produtos_vendidos+=item['quantidade']
    total_por_categoria[item['categoria']]+=valor
    unidades_por_categorias[item['categoria']]+=item['quantidade']
    cliente_compras[item['cliente']]+=item['quantidade']
    cliente_gastos[item['cliente']]+=valor
    total_por_regiao[item['regiao']]+=valor
    unidades_produtos[item['produto']]+=item['quantidade']
    pedidos_validos+=1
 pedido_por_status[item['status']]+=1
# calculando o ticket medio
ticket_medio=faturamento_total/pedidos_validos
# pegando o(s) cliente(s) que mais comprou
compras=[]
top_compras=max(cliente_compras.values())
for item in cliente_compras.items():
   if item[1]==top_compras:
      compras.append(item)
# pegando o(s) cliente(s) que mais gastou 
gastos=[]
top_gastos=max(cliente_gastos.values())
for item in cliente_gastos.items():
   if item[1]==top_gastos:
      gastos.append(item)
# pegando o produto mais vendido
mais_vendidos=[]
top_produto=max(unidades_produtos.values())
for item in unidades_produtos.items():
   if item[1]==top_produto:
      mais_vendidos.append(item)
    # organizando o print
print('==='*3,'RELATÓRIO VENDAS','==='*3)
print('---'*10)
print(f'Total de pedidos: {total_pedidos}')
print(f'Pedidos válidos: {pedidos_validos}')
print('---'*10)
print(f'Faturamento total: {faturamento_total} R$')
print(f'Produtos vendidos: {produtos_vendidos} unidades')
print('---'*10)
print('Pedidos por status:')
for dic in pedido_por_status.items():
   print(f'-{dic[0]}: {dic[1]}')
print('---'*10)
print('Quantidade por categoria:')
for info in unidades_por_categorias.items():
   print(f'-{info[0]}: {info[1]}')
print('---'*10)
print('Faturamento por categoria:')
for item in total_por_categoria.items():
   print(f'-{item[0]}: {item[1]} R$')
print('---'*10)
print('Cliente(s) que mais comprou(aram)')
for item in compras:
   print(f'-{item[0]}: {item[1]} unidades')
print('---'*10)
print('Cliente(s) que mais gastou(aram)')
for item in gastos:
   print(f'-{item[0]}: {item[1]} R$')
print('---'*10)
print('Quantidade por produto:')
for item in unidades_produtos.items():
   print(f'-{item[0]}: {item[1]}')
print('---'*10)
print('Faturamento por região:')
for info in total_por_regiao.items():
   print(f'-{info[0]}: {info[1]} R$')
print('---'*10)
print('Produto(s) mais vendido(s)')
for prod in mais_vendidos:
   print(f'-{prod[0]} {prod[1]} unidades')
print('---'*10)
print('Ticket Medio:')
print(f'{ticket_medio:.2f} R$')
print('==='*15)

