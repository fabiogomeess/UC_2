# RECUPERAÇÃO DE VEÍCULOS POR BATALHÃO

# IMPORTANDO BIBLIOTECAS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ENDEREÇO DA BASE DE DADOS
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# CRIANDO DATAFRAMES 
df_rec_del = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_rec_del_1 = df_rec_del[['aisp','ano','recuperacao_veiculos']]
# CRIANDO DATAFRAME RECUPERAÇÃO VEÍCULOS AGRUPADO PELOS ANOS DE 2024 E 2024
df_rec_del_1 = df_rec_del_1[df_rec_del_1['ano'].isin([2023,2024])]
df_rec_del_1 = df_rec_del_1.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

# CRIANDO ARRAY RECUPERAÇÃO DE VEÍCULOS
array_recuperacao_veiculos = np.array(df_rec_del_1['recuperacao_veiculos'])

# OBTENDO DADOS SOLICITADOS - ROUBO DE CARGA POR MUNICÍPIO

# MÉDIA 
media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)
# MEDIANA
mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)
# MAIOR NÚMERO DE CASOS
maior_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
# MENOR NÚMERO DE CASOS
menor_recuperacao_veiculos = np.min(array_recuperacao_veiculos)
# DISTANCIA ENTRE A MÉDIA E A MEDIANA
distancia = abs(((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos) * 100)
# AMPLITUDE ENTRE MAIOR E O MENOR NÚMERO DE CASOS
amplitude = maior_recuperacao_veiculos - menor_recuperacao_veiculos

# QUARTIS 
q1_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
q2_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
q3_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')

# IQR - HOMICÍDIO DOLOSO
iqr_recuperacao_veiculos = q3_recuperacao_veiculos - q1_recuperacao_veiculos # INTERVALO INTERQUANTIL

# LIMITES
limite_inferior_recuperacao_veiculos = q1_recuperacao_veiculos - (1.5 * iqr_recuperacao_veiculos)
limite_superior_recuperacao_veiculos = q3_recuperacao_veiculos + (1.5 * iqr_recuperacao_veiculos)

# BUSCANDO OUTLIERS - HOMICÍDIO DOLOSO
df_recuperacao_veiculos_outliers_inferiores = df_rec_del_1[df_rec_del_1['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculos]
df_recuperacao_veiculos_outliers_superiores = df_rec_del_1[df_rec_del_1['recuperacao_veiculos'] > limite_superior_recuperacao_veiculos]

# OBTENDO AS MEDIDAS DE DISPERSÃO DOS ROUBOS DE VEÍCULOS (PARA VER SE OS DADOS SÃ HOMOGENEOS OU HETEROGENEOS)
varianca_rec_veiculo = np.var(array_recuperacao_veiculos)
distancia_var_rec_veiculo = varianca_rec_veiculo / (media_recuperacao_veiculos**2) # ** -> significa potencia (elevado ao quadrado (²))
desvio_padrao_rec_veiculo = np.std(array_recuperacao_veiculos) # std -> para fazer a raiz quadrada de um conjunto de valores
coeficiente_var_rec_veiculo = desvio_padrao_rec_veiculo / media_recuperacao_veiculos # -> para verificar a proximidade entre os valores

# EXIBINDO BASE DE DADOS - RECUPERAÇÃO DE VEÍCULOS POR DELEGACIAS
print('--- TABELA DE RECUPERAÇÃO DE VEÍCULOS POR DELEGACIAS ---')
print(f'\n{df_rec_del_1}')

# EXIBINDO RESULTADOS EXTRAÍDOS PARA ANÁLISE DE DADOS - RECUPERAÇÃO DE VEÍCULOS
print('\n----- EXIBINDO RESULTADO DA PESQUISA - RECUPERAÇÃO DE VEÍCULOS POR DELEGACIA -----')
print(f"\nA média de Recuperação de Veículos é {media_recuperacao_veiculos}.")
print(f"\nA mediana de Recuperação de Veículos é {mediana_recuperacao_veiculos}.")
print(f"\nA distância entre a média e a mediana é {distancia}")
print(f"\nO maior número de casos: {maior_recuperacao_veiculos}.")
print(f"\nO menor número de casos: {menor_recuperacao_veiculos}.")
print(f"\nA amplitude é {amplitude}.")
print(f"\nLimite Superior de Recuperação de Veículos: {limite_superior_recuperacao_veiculos}.")
print(f"\nLimite Inferior de Recuperação de Veículos: {limite_inferior_recuperacao_veiculos}.")

print("\nVerificando Outliers")

if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculos_outliers_inferiores)
print("\n--- Outliers Superiores ---")
if len(df_recuperacao_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculos_outliers_superiores)

# VISUALIZANDO OS DADOS SOBRE  Recuperação de Veículos por Batalhão
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Recuperação de Veículos por Batalhão nos anos de 2023 e 2024')

# Posição 01: Gráfico de Recuperação de Veículos por Batalhão
plt.subplot(2,2,1)
plt.title('BoxPlot de Recuperação de Veículos por Batalhão')
plt.boxplot(array_recuperacao_veiculos,vert=False,showmeans=True)

# Posição 2: Histograma de Recuperação de Veículos por Batalhão
plt.subplot(2,2,2)
plt.title('Histograma de Recuperação de Veículos por Batalhão')
plt.hist(array_recuperacao_veiculos,bins=100,edgecolor='black')

# Posição 03: Lista de Recuperação de Veículos por Batalhão
plt.subplot(2,2,3)
df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.title("Ranking de Recuperação de Veículos por Batalhão com Outliers Superiores")
plt.barh(df_recuperacao_veiculos_outliers_superiores['aisp'].astype(str),df_recuperacao_veiculos_outliers_superiores['recuperacao_veiculos'])

# Posição 04: Medidas Descritivas de Recuperação de Veículos por Batalhão
plt.subplot(2,2,4)
plt.title('Medidas Descritivas de Recuperação de Veículos por Batalhão')
plt.axis('off')
plt.text(0.1,0.9,f'A média de Recuperação de Veículos é {media_recuperacao_veiculos}.',fontsize=12)
plt.text(0.1,0.8,f'A mediana de Recuperação de Veículos é {mediana_recuperacao_veiculos}.',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana é {distancia:.2f}%.',fontsize=12)
plt.text(0.1,0.6,f'O maior número de casos: {maior_recuperacao_veiculos}.',fontsize=12)
plt.text(0.1,0.5,f'O menor número de casos: {menor_recuperacao_veiculos}.',fontsize=12)
plt.text(0.1,0.4,f'A distancia entre a Variância e Média dos Roubos de Veículos é {distancia_var_rec_veiculo:.2f}.',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de Variação de Roubo de Veículos é {coeficiente_var_rec_veiculo:.2f}.',fontsize=12)

# EXIBINDO O PAINEL

plt.tight_layout()
plt.show()