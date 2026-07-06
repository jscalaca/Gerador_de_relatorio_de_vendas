import json
with open("vendas.json","r",encoding="utf-8") as arquivo:
    dados_vendas=json.load(arquivo)
pedido_por_status={}
faturamento_total=0
unidades_vendidas=0
total_por_categoria={}
pedidos_por_regiao={}
faturamento_por_regiao={}
total_pedidos=len(dados_vendas)
for item in dados_vendas:
 id_venda=item['id_pedido']
 data=item['data']
 cliente=item['cliente']
 cidade=item['cidade']
 regiao=item['regiao']
 produto=item['produto']
 categoria=item['categoria']
 unidades=item['quantidade']
 valor=item['valor_unitario']
 status=item['status']
 if status != "Cancelado":
   preco=unidades*valor
   faturamento_total+=preco
   unidades_vendidas+=unidades
 if status not in pedido_por_status:
     pedido_por_status[status]=0
 pedido_por_status[status]+=1
 if status != "Cancelado":
  preco=unidades*valor
  if categoria not in total_por_categoria:
     total_por_categoria[categoria]=0
  total_por_categoria[categoria]+=preco
  if regiao not in pedidos_por_regiao:
     pedidos_por_regiao[regiao]=0
  pedidos_por_regiao[regiao]+=1
  if regiao not in faturamento_por_regiao:
     faturamento_por_regiao[regiao]=0
  faturamento_por_regiao[regiao]+=preco
print('===='*2,'RELATORIO VENDAS','===='*2)
print(f'Total de Pedidos: {total_pedidos} pedidos')
print('==='*10)
print(f'Faturamento Total: {faturamento_total} R$')
print('==='*10)
print(f'Total de Produtos Vendidos: {unidades_vendidas} unidades')
print('==='*10)
print('Pedido Por Status')
print('---'*10)
for info in pedido_por_status.items():
   print(f'{info[0]}: {info[1]} pedidos')
print('==='*10)
print('Faturamento por Categoria')
print('---'*10)
for item in total_por_categoria.items():
   print(f'{item[0]}: {item[1]} R$')
print('==='*10)
print('Pedidos por Região')
print('---'*10)
for dic in pedidos_por_regiao.items():
   print(f'{dic[0]}: {dic[1]} Pedidos')
print('==='*10)
print('Faturamento por Região')
print('---'*10)
for info in faturamento_por_regiao.items():
   print(f'{info[0]}: {info[1]} R$')
print('==='*15)




