import json
def carregar_dados(dados='vendas.json'):
 """Carrega os dados para a análise"""
 try:
  with open(dados,"r",encoding="utf-8") as arquivo:
    dados_vendas=json.load(arquivo)
  return dados_vendas
 except FileNotFoundError:
   print(f"arquivo-{dados}-não encontrado")
