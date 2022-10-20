import pandas as pd
import requests


link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=100&$orderby=Data%20desc&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"

requisicao = requests.get(link)
info = requisicao.json()
tabela = pd.DataFrame(info["value"])
print(tabela)




