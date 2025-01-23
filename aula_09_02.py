# FAZER UMA ANALISE DE DADOS ESTATISTICAS DE SEGURANÇA: ROUBO DE VEICULO POR DELEGACIAS


# Importando Biblioteca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

 # CRIANDO O DATAFRAME POR MUNICIPIO
df_roubo_delegacia = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_delegacia_1 = df_roubo_delegacia[['cisp','roubo_veiculo']]
df_roubo_delegacia_1 = df_roubo_delegacia_1.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Criando um array Roubo de Veículos por Delegacia (SOMENTE PARA OS NÚMEROS QUE SERÃO ANALISADOS)
array_roubo_delegacia = np.array(df_roubo_delegacia_1['roubo_veiculo'])

# OBTENDO DADOS SOLICITADOS - Roubo de Veículos por Delegacia

# MÉDIA 
media_roubo_delegacia = np.mean(array_roubo_delegacia)
# MEDIANA
mediana_roubo_delegacia = np.median(array_roubo_delegacia)
# MAIOR NÚMERO DE CASOS
maior_roubo_delegacia = np.max(array_roubo_delegacia)
# MENOR NÚMERO DE CASOS
menor_roubo_delegacia = np.min(array_roubo_delegacia)
# DISTANCIA ENTRE A MÉDIA E A MEDIANA
distancia = abs(((media_roubo_delegacia - mediana_roubo_delegacia) / mediana_roubo_delegacia) * 100)
# AMPLITUDE ENTRE MAIOR E O MENOR NÚMERO DE CASOS
amplitude = maior_roubo_delegacia - menor_roubo_delegacia

# QUARTIS 
q1_roubo_delegacia = np.quantile(array_roubo_delegacia, 0.25, method='weibull')
q2_roubo_delegacia = np.quantile(array_roubo_delegacia, 0.50, method='weibull')
q3_roubo_delegacia = np.quantile(array_roubo_delegacia, 0.75, method='weibull')

# IQR - ROUBO DE VEÍCULOS
iqr_roubo_delegacia = q3_roubo_delegacia - q1_roubo_delegacia # INTERVALO INTERQUANTIL

# LIMITES
limite_inferior_roubo_delegacia = q1_roubo_delegacia - (1.5 * iqr_roubo_delegacia)
limite_superior_roubo_delegacia = q3_roubo_delegacia + (1.5 * iqr_roubo_delegacia)

# BUSCANDO OUTLIERS - ROUBO DE VEÍCULOS
df_roubo_veiculo_outliers_inferiores = df_roubo_delegacia_1[df_roubo_delegacia_1['roubo_veiculo'] < limite_inferior_roubo_delegacia]
df_roubo_veiculo_outliers_superiores = df_roubo_delegacia_1[df_roubo_delegacia_1['roubo_veiculo'] > limite_superior_roubo_delegacia]

# OBTENDO AS MEDIDAS DE DISPERSÃO DOS ROUBOS DE VEÍCULOS (PARA VER SE OS DADOS SÃ HOMOGENEOS OU HETEROGENEOS)
varianca_roubo_veiculo = np.var(array_roubo_delegacia)
distancia_var_roubo_veiculo = varianca_roubo_veiculo / (media_roubo_delegacia**2) # ** -> significa potencia (elevado ao quadrado (²))
desvio_padrao_roubo_veiculo = np.std(array_roubo_delegacia) # std -> para fazer a raiz quadrada de um conjunto de valores
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_delegacia # -> para verificar a proximidade entre os valores

# EXIBINDO A BASE DE DADOS - ROUBO DE VEÍCULOS POR DELEGACIA
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_roubo_delegacia_1)

# EXIBINDO RESULTADOS EXTRAÍDOS PARA ANÁLISE DE DADOS - ROUBO DE VEÍCULOS POR DELEGACIA
print('\n----- EXIBINDO RESULTADO DA PESQUISA - ROUBO DE VEÍCULOS POR DELEGACIA -----')
print(f"\nA média de Roubos de Veículos é {media_roubo_delegacia:.0f}.")
print(f"\nA mediana de Roubos de Veículos é {mediana_roubo_delegacia:.0f}.")
print(f"\nA distância entre a média e a mediana é {distancia:.2f}%.")
print(f"\nO maior número de casos: {maior_roubo_delegacia}.")
print(f"\nO menor número de casos: {menor_roubo_delegacia}.")
print(f"\nA amplitude é {amplitude}.")
print(f"\nLimite Superior dos Roubos de Veículos: {limite_superior_roubo_delegacia:.0f}.")
print(f"\nLimite Inferior dos Roubos de Veículos: {limite_inferior_roubo_delegacia:.0f}.")

print("\nVerificando Outliers")

if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print("\n--- Outliers Superiores ---")
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores)

# VISUALIZANDO OS DADOS SOBRE ROUBO DE VEÍCULOS POR DELEGACIAS
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Roubo de Veículos por Delegacia')

# Posição 01: Gráfico dos ROUBO DE VEÍCULOS POR DELEGACIAS
plt.subplot(2,2,1)
plt.title('BoxPlot dos Roubos de Veículos por Delegacia')
plt.boxplot(array_roubo_delegacia,vert=False,showmeans=True)

# Posição 2: Histograma dos ROUBO DE VEÍCULOS POR DELEGACIAS
plt.subplot(2,2,2)
plt.title('Histograma dos Roubos de Veículos por Delegacia')
plt.hist(array_roubo_delegacia,bins=100,edgecolor='black')

# Posição 03: Lista dos ROUBO DE VEÍCULOS POR DELEGACIAS
plt.subplot(2,2,3)
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title("Ranking dos Roubos de Veículos por Delegacia com Outliers Superiores")
plt.barh(df_roubo_veiculo_outliers_superiores['cisp'].astype(str),df_roubo_veiculo_outliers_superiores['roubo_veiculo'])

# Posição 04: Medidas Descritivas dos Roubos de Veículos por Delegacia
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'A média dos Roubos de Veículos é {media_roubo_delegacia:.0f}.',fontsize=12)
plt.text(0.1,0.8,f'A mediana dos Roubos de Veículos é {mediana_roubo_delegacia:.0f}.',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana é {distancia:.2f}%.',fontsize=12)
plt.text(0.1,0.6,f'O maior número de casos: {maior_roubo_delegacia}.',fontsize=12)
plt.text(0.1,0.5,f'O menor número de casos: {menor_roubo_delegacia}.',fontsize=12)
plt.text(0.1,0.4,f'A distancia entre a Variância e Média dos Roubos de Veículos é {distancia_var_roubo_veiculo:.2f}.',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de Variação de Roubo de Veículos é {coeficiente_var_roubo_veiculo:.2f}.',fontsize=12)

# EXIBINDO O PAINEL

plt.tight_layout()
plt.show()