import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# IMPORTANDO A BASE DE DADOS BaseDPEvolucaoMensalCisp
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# CRIANDO O DATAFRAME Delegacias - Roubo de Veículos
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']] # CISP é delegacia
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index() # DATAFRAME CONSOLIDADO, DADOS CONSOLIDADOS POR DELEGACIA POR OCORRENCIA ESPECIFICA

# EXIBINDO A BASE DE DADOS Delegacias - Roubo de Veículos
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_roubo_veiculo.head())