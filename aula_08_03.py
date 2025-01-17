# FAZER UMA ANALISE DE DADOS ESTATISTICAS DE SEGURANÇA: série histórica mensal por área de delegacia desde 01/2003

# ROUBO DE CARGA POR MUNICÍPIO 

# Importando Biblioteca
import pandas as pd
import numpy as np

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

 # CRIANDO O DATAFRAME POR MUNICIPIO
df_mp = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')
df_mp_1 = df_mp[['munic','roubo_carga']]
df_mp_1 = df_mp_1.groupby(['munic']).sum(['roubo_carga']).reset_index()

# Criando um array Roubo de Carga (SOMENTE PARA OS NÚMEROS QUE SERÃO ANALISADOS)
array_roubo_carga = np.array(df_mp_1['roubo_carga'])

# OBTENDO DADOS SOLICITADOS - ROUBO DE CARGA POR MUNICÍPIO

# MÉDIA 
media_roubo_carga = np.mean(array_roubo_carga)
# MEDIANA
mediana_roubo_carga = np.median(array_roubo_carga)
# MAIOR NÚMERO DE CASOS
maior_roubo_carga = np.max(array_roubo_carga)
# MENOR NÚMERO DE CASOS
menor_roubo_carga = np.min(array_roubo_carga)
# DISTANCIA ENTRE A MÉDIA E A MEDIANA
distancia = abs(((media_roubo_carga - mediana_roubo_carga) / mediana_roubo_carga))
# AMPLITUDE ENTRE MAIOR E O MENOR NÚMERO DE CASOS
amplitude = maior_roubo_carga - menor_roubo_carga

# QUARTIS 
q1_roubo_carga = np.quantile(array_roubo_carga, 0.25, method='weibull')
q2_roubo_carga = np.quantile(array_roubo_carga, 0.50, method='weibull')
q3_roubo_carga = np.quantile(array_roubo_carga, 0.75, method='weibull')

# IQR - HOMICÍDIO DOLOSO
iqr_roubo_carga = q3_roubo_carga - q1_roubo_carga # INTERVALO INTERQUANTIL

# LIMITES
limite_inferior_roubo_carga = q1_roubo_carga - (1.5 * iqr_roubo_carga)
limite_superior_roubo_carga = q3_roubo_carga + (1.5 * iqr_roubo_carga)

# BUSCANDO OUTLIERS - HOMICÍDIO DOLOSO
df_roubo_carga_outliers_inferiores = df_mp_1[df_mp['roubo_carga'] < limite_inferior_roubo_carga]
df_roubo_carga_outliers_superiores = df_mp_1[df_mp['roubo_carga'] > limite_superior_roubo_carga]

# EXIBINDO A BASE DE DADOS Upps - ROUBO DE CARGA POR MUNICÍPIO
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_mp_1)

# EXIBINDO RESULTADOS EXTRAÍDOS PARA ANÁLISE DE DADOS - HOMICÍDIO DOLOSO
print('\n----- EXIBINDO RESULTADO DA PESQUISA - HOMICÍDIO DOLOSO UPPS -----')
print(f"\nA média de Homicídios Dolosos é {media_roubo_carga}.")
print(f"\nA mediana de Homicídios Dolosos é {mediana_roubo_carga}.")
print(f"\nA distância entre a média e a mediana é {distancia}")
print(f"\nO maior número de casos: {maior_roubo_carga}.")
print(f"\nO menor número de casos: {menor_roubo_carga}.")
print(f"\nA amplitude é {amplitude}.")
print(f"\nLimite Superior dos Homicídios: {limite_superior_roubo_carga}.")
print(f"\nLimite Inferior dos Homicídios: {limite_inferior_roubo_carga}.")

print("\nVerificando Outliers")

if len(df_roubo_carga_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_carga_outliers_inferiores)
print("\n--- Outliers Superiores ---")
if len(df_roubo_carga_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_carga_outliers_superiores)
