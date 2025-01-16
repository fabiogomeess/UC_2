# ANÁLISE DE DADOS UPPS (Colunas -> upp e hom_doloso)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# IMPORTANDO BASE DE DADOS (UppEvolucaoMensalDeTitulos)
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv'

# CRIANDO O DATAFRAME UPPS
df_upp = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_upp_hom_doloso = df_upp[['upp','hom_doloso']]
df_upp_hom_doloso = df_upp_hom_doloso.groupby(['upp']).sum(['hom_doloso']).reset_index()

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
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')

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
print(f"\nA mediana de Homicídios Dolosos é {mediana_hom_doloso}.")
print(f"\nA distância entre a média e a mediana é {distancia}")
print(f"\nO maior número de casos: {maior_hom_doloso}.")
print(f"\nO menor número de casos: {menor_hom_doloso}.")
print(f"\nA amplitude é {amplitude}.")
print(f"\nLimite Superior dos Homicídios: {limite_superior_hom_doloso}.")
print(f"\nLimite Inferior dos Homicídios: {limite_inferior_hom_doloso}.")

print("\nVerificando Outliers")
if len(df_hom_doloso_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_hom_doloso_outliers_superiores)

if len(f"\ndf_hom_doloso_outliers_superiores") == 0:
    print("Não existem outliers superiores")
else:
    print(df_hom_doloso_outliers_superiores)

# VISUALIZANDO OS DADOS SOBRE HOMICÍDIO DOLOSO
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Homicídios Dolosos por UPPs')

# Posição 01: Gráfico dos Homicídios Dolosos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Homicidios Dolosos')
plt.boxplot(array_hom_doloso,vert=False,showmeans=True)

# Posição 2: Histograma dos Homicídios Dolosos
plt.subplot(2,2,2)
plt.title('Histograma dos Homicídios Dolosos')
plt.hist(array_hom_doloso,bins=100,edgecolor='black')

# Posição 03: Lista de UPP's com Outliers
plt.subplot(2,2,3)
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
plt.title("Ranking das UPP's com Outliers Superiores")
plt.barh(df_hom_doloso_outliers_superiores_order['upp'],df_hom_doloso_outliers_superiores_order['hom_doloso'])

# Posição 04: Medidas Descritivas dos Homicídios Dolosos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Homícidos Dolosos')
plt.axis('off')
plt.text(0.1,0.9,f'A média de Homicídios Dolosos é {media_hom_doloso}.',fontsize=12)
plt.text(0.1,0.8,f'A mediana de Homicídios Dolosos é {mediana_hom_doloso}.',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana é {distancia}.',fontsize=12)
plt.text(0.1,0.6,f'O maior número de casos: {maior_hom_doloso}.',fontsize=12)
plt.text(0.1,0.5,f'O menor número de casos: {menor_hom_doloso}.',fontsize=12)
plt.text(0.1,0.4,f'A amplitude é {amplitude}.',fontsize=12)
plt.text(0.1,0.3,f'Limite Superior dos Homicídios: {limite_superior_hom_doloso}.',fontsize=12)
plt.text(0.1,0.2,f'Limite Inferior dos Homicídios: {limite_inferior_hom_doloso}.',fontsize=12)

# EXIBINDO O PAINEL

plt.tight_layout()
plt.show()