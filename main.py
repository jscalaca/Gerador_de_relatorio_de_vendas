import json
with open("vendas.json","r",encoding="utf-8") as arquivo:
    dados_vendas=json.load(arquivo)
pedido_por_status={}
faturamento_total=0
unidades_vendidas=0
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
print('===='*2,'RELATORIO VENDAS','===='*2)
print(f'Total de Pedidos: {total_pedidos} pedidos')
print('---'*10)
print(f'Faturamento Total: {faturamento_total} R$')
print('---'*10)
print(f'Total de Produtos Vendidos: {unidades_vendidas} unidades')
print('---'*10)
print('Pedido Por Status')
for info in pedido_por_status.items():
   print(f'{info[0]}: {info[1]} pedidos')
print('==='*15)



