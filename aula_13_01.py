#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame recuperação de veículos
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_comercio = df_ocorrencias[['cisp','roubo_comercio']]
df_roubo_comercio = df_roubo_comercio.groupby(['cisp']).sum(['roubo_comercio']).reset_index()

# Criando o DataFrame Roubo Comércio e Roubo Residência
df_roubo_com_res = df_ocorrencias[['cisp','roubo_comercio','roubo_residencia']]
df_roubo_com_res = df_roubo_com_res.groupby(['cisp']).sum(['roubo_comercio','roubo_residencia']).reset_index()

# Criando Dataframe 2023 e 2024
df_rob_com_2023_2024 = df_ocorrencias[['cisp','ano','roubo_comercio']]
df_rob_com_2023_2024 = df_rob_com_2023_2024[df_rob_com_2023_2024['ano'].isin([2023, 2024])]
df_rob_com_2023_2024 = df_rob_com_2023_2024.groupby(['cisp']).sum(['roubo_comercio']).reset_index()

# EXIBINDO DATAFRAME ROUBO COMÉRCIO
print('\n--- EXIBINDO DATAFRAME ROUBO COMÉRCIO ---')
print(df_roubo_comercio)

# EXIBINDO BASE DE DADOS ROUBO COMÉRCIO E RESIDÊNCIA
print('\n---- EXIBINDO A BASE DE DADOS ROUBO COMÉRCIO E RESIDÊNCIA-----')
print(df_roubo_com_res.head())

# CRIANDO ARRAY ROUBO COMÉRCIO
array_roubo_comercio = np.array(df_roubo_comercio["roubo_comercio"])

# OBTENDO A MÉDIA ROUBO COMÉRCIO
media_roubo_comercio = np.mean(array_roubo_comercio)

# OBTENDO A MEDIANA ROUBO COMÉRCIO
mediana_roubo_comercio = np.median(array_roubo_comercio)

# OBTENDO A DISTÂNCIA ENTRE A MÉDIA E A MEDIANA ROUBO COMÉRCIO
distancia_roubo_comercio = abs((media_roubo_comercio - mediana_roubo_comercio) / mediana_roubo_comercio) * 100

# OBTENDO O MÁXIMO E O MÍNIMO ROUBO COMÉRCIO
maximo_roubo_comercio = np.max(array_roubo_comercio)
minimo_roubo_comercio = np.min(array_roubo_comercio)

# OBTENDO A AMPLITUDE ROUBO COMÉRCIO
amplitude_roubo_comercio = maximo_roubo_comercio - minimo_roubo_comercio

# OBTENDO OS QUARTIS ROUBO COMÉRCIO - Método weibull
q1_roubo_comercio = np.quantile(array_roubo_comercio, 0.25, method='weibull')
q2_roubo_comercio = np.quantile(array_roubo_comercio, 0.50, method='weibull')
q3_roubo_comercio = np.quantile(array_roubo_comercio, 0.75, method='weibull')
iqr_roubo_comercio = q3_roubo_comercio - q1_roubo_comercio

# IDENTIFICANDO OS OUTLIERS SUPERIORES E INFERIORES ROUBO COMÉRCIO
limite_superior_roubo_comercio = q3_roubo_comercio + (1.5 * iqr_roubo_comercio)
limite_inferior_roubo_comercio = q1_roubo_comercio - (1.5 * iqr_roubo_comercio)

# FILTRANDO O DATAFRAME ROUBO COMÉRCIO
df_roubo_comercio_outliers_superiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] > limite_superior_roubo_comercio]
df_roubo_comercio_outliers_inferiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] < limite_inferior_roubo_comercio]

# Obtendo as medidas de dispersão dos recuperação de veículos
variancia_roubo_comercio = np.var(array_roubo_comercio)
distancia_var_roubo_comercio = variancia_roubo_comercio / (media_roubo_comercio**2)

desvio_padrao_roubo_comercio = np.std(array_roubo_comercio)
coeficiente_var_roubo_comercio = desvio_padrao_roubo_comercio / media_roubo_comercio

# -------------------------------------------------------------------------------------------------------

# Criando o array Roubo Residência
array_roubo_residencia = np.array(df_roubo_com_res["roubo_residencia"])

# Obtendo a média Roubo Residência
media_roubo_residencia = np.mean(array_roubo_residencia)

# Obtendo a mediana Roubo Residência
mediana_roubo_residencia = np.median(array_roubo_residencia)

# Obtendo a distância entre a média e a mediana Roubo Residência
distancia_roubo_residencia = abs((media_roubo_residencia - mediana_roubo_residencia) / mediana_roubo_residencia) * 100

# Obtendo o máximo e o mínimo Roubo Residência
maximo_roubo_residencia = np.max(array_roubo_residencia)
minimo_roubo_residencia = np.min(array_roubo_residencia)

# Obtendo a amplitude Roubo Residência
amplitude_roubo_residencia = maximo_roubo_residencia - minimo_roubo_residencia

# Obtendo os Quartis Roubo Residência - Método weibull
q1_roubo_residencia = np.quantile(array_roubo_residencia, 0.25, method='weibull')
q2_roubo_residencia = np.quantile(array_roubo_residencia, 0.50, method='weibull')
q3_roubo_residencia = np.quantile(array_roubo_residencia, 0.75, method='weibull')
iqr_roubo_residencia = q3_roubo_residencia - q1_roubo_residencia

# Identificando os outliers superiores e inferiores Roubo Residência
limite_superior_roubo_residencia = q3_roubo_residencia + (1.5 * iqr_roubo_residencia)
limite_inferior_roubo_residencia = q1_roubo_residencia - (1.5 * iqr_roubo_residencia)

# Filtrando o DataFrame Roubo Residência
df_roubo_residencia_outliers_superiores = df_roubo_com_res[df_roubo_com_res['roubo_residencia'] > limite_superior_roubo_residencia]
df_roubo_residencia_outliers_inferiores = df_roubo_com_res[df_roubo_com_res['roubo_residencia'] < limite_inferior_roubo_residencia]

# Obtendo as medidas de dispersão dos Roubo Residência
variancia_roubo_residencia = np.var(array_roubo_residencia)
distancia_var_roubo_residencia = variancia_roubo_residencia / (media_roubo_residencia**2)

desvio_padrao_roubo_residencia = np.std(array_roubo_residencia)
coeficiente_var_roubo_residencia = desvio_padrao_roubo_residencia / media_roubo_residencia

# Obtendo a correlação entre as recuperações e os roubos de veículos
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação
correl_roubo_com_res = np.corrcoef(df_roubo_com_res['roubo_comercio'],df_roubo_com_res['roubo_residencia'])[0,1]

# Exibindo os dados sobre as recuperações de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE ROUBO A COMÉRCIO -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"Média Roubo Comércio: {media_roubo_comercio:.0f}")
print(f"Mediana Roubo Comércio: {mediana_roubo_comercio:.0f}")
print(f"Distância entre a média e a mediana Roubo Comércio: {distancia_roubo_comercio:.2f} %")
print(f"Menor valor Roubo Comércio: {minimo_roubo_comercio:.0f}")
print(f"Maior valor Roubo Comércio: {maximo_roubo_comercio:.0f}")
print(f"Amplitude Roubo Comércio {amplitude_roubo_comercio:.0f}")
print(f"Valor do q1 - 25% Roubo Comércio: {q1_roubo_comercio:.0f}")
print(f"Valor do q2 - 50% Roubo Comércio: {q2_roubo_comercio:.0f}")
print(f"Valor do q3 - 75% Roubo Comércio: {q3_roubo_comercio:.0f}")
print(f"Valor do iqr = q3 - q1 Roubo Comércio: {iqr_roubo_comercio:.0f}")
print(f"Limite inferior Roubo Comércio: {limite_inferior_roubo_comercio:.0f}")
print(f"Limite superior Roubo Comércio: {limite_superior_roubo_comercio:.0f}")
print(f"Variância Roubo Comércio: {variancia_roubo_comercio:.0f}")
print(f"Distância da variância X média Roubo Comércio: {distancia_var_roubo_comercio:.0f}")
print(f"Desvio padrão Roubo Comércio: {desvio_padrao_roubo_comercio:.0f}")
print(f"Coeficiente de variação Roubo Comércio: {coeficiente_var_roubo_comercio:.0f}")
print(f'{correl_roubo_com_res:.2f}%')

print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_comercio_outliers_inferiores) == 0:
    print("\nNão existem outliers inferiores")
else:
    print(df_roubo_comercio_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_comercio_outliers_superiores) == 0:
    print("\nNão existem outliers superiores")
else:
    print(df_roubo_comercio_outliers_superiores)

# VISUALIZANDO OS DADOS SOBRE ROUBO COMÉRCIO
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(4,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Roubo em Comércio',fontsize=18)

if len(df_roubo_comercio_outliers_superiores) != 0 or len(df_roubo_comercio_outliers_inferiores) != 0:
    # posição 01: GRÁFICO ROUBO COMÉRCIO
    plt.subplot(4,2,1)
    plt.title('BoxPlot Roubo a Comércio')
    plt.boxplot(array_roubo_comercio,vert=False,showmeans=True)

    # posição 02: HISTOGRAMA ROUBO COMÉRCIO
    plt.subplot(4,2,2)
    plt.title('Histograma Roubo a Comércio')
    plt.hist(array_roubo_comercio,bins=100,edgecolor='black')

    # posição 03: RANKING ROUBO COMÉRCIO
    plt.subplot(4,2,3)
    df_roubo_comercio_outliers_superiores_order = df_roubo_comercio_outliers_superiores.sort_values(by='roubo_comercio',ascending=True)
    plt.title('Ranking Roubo a Comércio com Outliers Superiores')
    plt.barh(df_roubo_comercio_outliers_superiores['cisp'].astype(str),df_roubo_comercio_outliers_superiores['roubo_comercio'])

    # posição 04: MEDIDAS DESCRITIVAS ROUBO COMÉRCIO
    plt.subplot(4,2,4)
    plt.title('Medidas Descritivas Roubo a Comércio')
    plt.axis('off')
    plt.text(0.1,0.9,f'Média Roubo a Comércio: {media_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'Mediana Roubo a Comércio: {mediana_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'Distância entre Média e Mediana Roubo a Comércio: {distancia_roubo_comercio:.2f}%',fontsize=12)
    plt.text(0.1,0.6,f'Maior valor Roubo a Comércio: {maximo_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'Menor valor Roubo a Comércio: {minimo_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'Distância entre a Variância e Média Roubo a Comércio: {distancia_var_roubo_comercio:.2f}',fontsize=12)
    plt.text(0.1,0.3,f'Coeficiente de variação Roubo a Comércio: {coeficiente_var_roubo_comercio:.2f}',fontsize=12)

else:
    # posição 01: GRÁFICO DOS MENORES ROUBOS A COMÉRCIO
    df_roubo_comercio_order_menor = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] < q1_roubo_comercio]
    df_roubo_comercio_order = df_roubo_comercio_order_menor.sort_values(by='roubo_comercio',ascending=False).head(10)
    plt.subplot(4,2,1)
    plt.title('Top 10 Delegacias com Menores Valores')
    plt.bar(df_roubo_comercio_order['cisp'].astype(str),df_roubo_comercio_order['roubo_comercio'])

    # posição 02: GRÁFICO DOS MAIORES ROUBOS A COMÉRCIO
    df_roubo_comercio_order_maior = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] > q3_roubo_comercio]
    df_roubo_comercio_order = df_roubo_comercio_order_maior.sort_values(by='roubo_comercio',ascending=True).tail(10)
    plt.subplot(4,2,2)
    plt.title('Top 10 Delegacias com Maiores Valores')
    plt.bar(df_roubo_comercio_order['cisp'].astype(str),df_roubo_comercio_order['roubo_comercio'])

    # posição 03: GRÁFICO ACIMA DA MÉDIA ROUBOS A COMÉRCIO
    df_roubo_comercio_order_maior = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] > media_roubo_comercio]
    df_roubo_comercio_order = df_roubo_comercio_order_maior.sort_values(by='roubo_comercio',ascending=True)
    plt.subplot(4,2,3)
    plt.title('Acumulado acima da média das ocorrências de Roubo a Comércio')
    plt.bar(df_roubo_comercio_order['cisp'].astype(str),df_roubo_comercio_order['roubo_comercio'])
    

    # posição 04: HISTOGRAMA ROUBO COMÉRCIO
    plt.subplot(4,2,4)
    plt.title('Histograma das ocorrências de Roubo a Comércio')
    plt.hist(array_roubo_comercio,bins=100,edgecolor='black')

    # posição 05: Medidas descritivas dos Roubos de Veículos
    plt.subplot(4,2,5)
    plt.title('Correlação Roubo a Comércio e Residência')
    plt.scatter(df_roubo_com_res['roubo_comercio'],df_roubo_com_res['roubo_residencia'])
    plt.xlabel('Roubo Comércio')
    plt.ylabel('Roubo Residência')

    # posição 06: GRÁFICO RANKING ROUBO COMÉRCIO 2023 E 2024
    plt.subplot(4,2,6)
    df_rou_com_23_24_order = df_rob_com_2023_2024.sort_values(by='roubo_comercio',ascending=True).tail(10)
    plt.title('Top 10 Ranking das Delegacias 2023 e 2024')
    plt.bar(df_rou_com_23_24_order['cisp'].astype(str),df_rou_com_23_24_order['roubo_comercio'])
    plt.xlabel('Delegacia')
    plt.ylabel('Número de Roubo')

    # posição 07: Medidas descritivas Roubo Comércio
    plt.subplot(4,2,7)
    plt.title('Medidas Descritivas Roubo a Comércio')
    plt.axis('off')
    plt.text(0.1,0.9,f'Média Roubo a Comércio: {media_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'Mediana Roubo a Comércio: {mediana_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'Distância entre Média e Mediana Roubo a Comércio: {distancia_roubo_comercio:.2f}%',fontsize=12)
    plt.text(0.1,0.6,f'Maior valor Roubo a Comércio: {maximo_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'Menor valor Roubo a Comércio: {minimo_roubo_comercio:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'Distância entre a Variância e Média Roubo a Comércio: {distancia_var_roubo_comercio:.2f}',fontsize=12)
    plt.text(0.1,0.3,f'Coeficiente de variação Roubo a Comércio: {coeficiente_var_roubo_comercio:.2f}',fontsize=12)

    # posição 08: Medidas descritivas dos Roubo Residência
    plt.subplot(4,2,8)
    plt.title('Medidas Descritivas Roubo a Residência')
    plt.axis('off')
    plt.text(0.1,0.9,f'Média Roubo a Residência: {media_roubo_residencia:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'Mediana Roubo a Residência: {mediana_roubo_residencia:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'Distância entre Média e Mediana Roubo a Residência: {distancia_roubo_residencia:.2f}%',fontsize=12)
    plt.text(0.1,0.6,f'Maior valor Roubo a Residência: {maximo_roubo_residencia:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'Menor valor Roubo a Residência: {minimo_roubo_residencia:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'Distância entre a Variância e Média Roubo a Residência: {distancia_var_roubo_residencia:.2f}',fontsize=12)
    plt.text(0.1,0.3,f'Coeficiente de variação Roubo a Residência: {coeficiente_var_roubo_residencia:.2f}',fontsize=12)

     
# Exibindo o Painel
plt.tight_layout()
plt.show()