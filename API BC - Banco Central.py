# Databricks notebook source
!pip install requests

# COMMAND ----------

import requests 
link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$orderby=Data%20desc&$format=json"
requisicao = requests.get(link)
informacoes = requisicao.json()  


# COMMAND ----------

##tabela_final = pd.DataFrame()
##pular_indice = 0


##while True:
##link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip=0&$orderby=Data%20desc&$format=json"
##requisicao = requests.get(link)
##informacoes = requisicao.json()
##tabela = pd.DataFrame(informacoes["value"])
##if len(informacoes['value']) < 1:
  ##tabela_final = pd.concat([tabela_final, tabela])
 ## pular_indice = pular_indice + 10000

# COMMAND ----------

print"(informacoes)

# COMMAND ----------

import pprint 

# COMMAND ----------

pprint.pprint(informacoes)

# COMMAND ----------

import pandas as pd
tabela = pd.DataFrame(informacoes["value"])
tabela["Quantidade"] = tabela["Quantidade"].map("{:,}".format)
#tabela["Valor"] = tabela["Valor"].map("R${:,.2f}".format)

# COMMAND ----------

display(tabela)
