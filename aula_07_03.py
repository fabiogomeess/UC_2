# ANÁLISE DE DADOS UPPS (Colunas -> upp e hom_doloso)
import pandas as pd
import numpy as np

# IMPORTANDO BASE DE DADOS (UppEvolucaoMensalDeTitulos)
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv'

# CRIANDO O DATAFRAME UPPS
df_upp = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_upp_hom_doloso = df_upp[['upp','hom_doloso']]
df_upp_hom_doloso = df_upp_hom_doloso.groupby(['upp']).sum(['hom_doloso']).reset_index

# Criando um array Homicidio Doloso (SOMENTE PARA OS NÚMEROS QUE SERÃO ANALISADOS)
array_hom_doloso = np.array(df_upp_hom_doloso['hom_doloso'])

# OBTENDO DADOS SOLICITADOS - HOMICÍDIO DOLOSO

# MÉDIA 
media_hom_doloso = np.mean(array_hom_doloso)
# MEDIANA
mediana_hom_doloso = np.median(array_hom_doloso)
# MAIOR NÚMERO DE CASOS
maior_hom_doloso = np.max(array_hom_doloso)
# MENOR NÚMERO DE CASOS
menor_hom_doloso = np.min(array_hom_doloso)
# DISTANCIA ENTRE A MÉDIA E A MEDIANA
distancia = abs(((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso))
# AMPLITUDE ENTRE MAIOR E O MENOR NÚMERO DE CASOS
amplitude = maior_hom_doloso - menor_hom_doloso

# QUARTIS 
q1_hom_doloso = np.quantile(array_hom_doloso, 0,25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0,50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0,75, method='weibull')

# IQR - HOMICÍDIO DOLOSO
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso # INTERVALO INTERQUANTIL

# LIMITES
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)

# BUSCANDO OUTLIERS - HOMICÍDIO DOLOSO
df_hom_doloso_outliers_inferiores = df_upp_hom_doloso[df_upp_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]
df_hom_doloso_outliers_superiores = df_upp_hom_doloso[df_upp_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]

# EXIBINDO A BASE DE DADOS Upps - Homicido Dosolo
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_upp_hom_doloso)

# EXIBINDO RESULTADOS EXTRAÍDOS PARA ANÁLISE DE DADOS - HOMICÍDIO DOLOSO
print('\n----- EXIBINDO RESULTADO DA PESQUISA - HOMICÍDIO DOLOSO UPPS -----')
print(f"\nA média de Homicídios Dolosos é {media_hom_doloso}.")