# Crimes Violentos Letais Intencionais – CVLI - 2023 e 2024

# IMPORTANDO BIBLICOTECAS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ENDEREÇO DA BASE DE DADOS
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv' 

3 # CRIANDO DATAFRAME

df_cvli = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli_1 = df_cvli[['aisp','ano','cvli']]
# CRIANDO DATAFRAME RECUPERAÇÃO VEÍCULOS AGRUPADO PELOS ANOS DE 2024 E 2024
df_cvli_1 = df_cvli_1[df_cvli_1['ano'].isin([2023,2024])]
df_cvli_1 = df_cvli_1.groupby(['aisp']).sum(['cvli']).reset_index()

# CRIANDO ARRAY CVLI
array_cvli = np.array(df_cvli_1['cvli'])

# OBTENDO DADOS SOLICITADOS - Crimes Violentos Letais Intencionais

# MÉDIA 
media_cvli = np.mean(array_cvli)
# MEDIANA
mediana_cvli = np.median(array_cvli)
# MAIOR NÚMERO DE CASOS
maior_cvli = np.max(array_cvli)
# MENOR NÚMERO DE CASOS
menor_cvli = np.min(array_cvli)
# DISTANCIA ENTRE A MÉDIA E A MEDIANA
distancia = abs(((media_cvli - mediana_cvli) / mediana_cvli) * 100)
# AMPLITUDE ENTRE MAIOR E O MENOR NÚMERO DE CASOS
amplitude = maior_cvli - menor_cvli

# QUARTIS 
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')

# IQR - CVLI
iqr_cvli = q3_cvli - q1_cvli # INTERVALO INTERQUANTIL

# LIMITES
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)

# BUSCANDO OUTLIERS - CVLI
df_cvli_outliers_inferiores = df_cvli_1[df_cvli_1['cvli'] < limite_inferior_cvli]
df_cvli_outliers_superiores = df_cvli_1[df_cvli_1['cvli'] > limite_superior_cvli]

# OBTENDO AS MEDIDAS DE DISPERSÃO DOS CVLIs (PARA VER SE OS DADOS SÃO HOMOGENEOS OU HETEROGENEOS)
varianca_cvli = np.var(array_cvli)
distancia__var_cvli = varianca_cvli / (media_cvli**2) # ** -> significa potencia (elevado ao quadrado (²))
desvio_padrao_cvli = np.std(array_cvli) # std -> para fazer a raiz quadrada de um conjunto de valores
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli # -> para verificar a proximidade entre os valores

# EXIBINDO DATAFRAME
print("--- EXIBINDO TABELA CVLI ---")
print(f'\n{df_cvli_1}')


# EXIBINDO RESULTADOS EXTRAÍDOS PARA ANÁLISE DE DADOS - Crimes Violentos Letais Intencionais
print('\n----- EXIBINDO RESULTADO DA PESQUISA - RECUPERAÇÃO DE VEÍCULOS POR DELEGACIA -----')
print(f"\nA média sobre Crimes Violentos Letais Intencionais é {media_cvli:.2f}.")
print(f"\nA mediana sobre Crimes Violentos Letais Intencionais é {mediana_cvli}.")
print(f"\nA distância entre a média e a mediana é {distancia:.2f}%")
print(f"\nO maior número de casos: {maior_cvli}.")
print(f"\nO menor número de casos: {menor_cvli}.")
print(f"\nA amplitude é {amplitude}.")
print(f"\nLimite Superior sobre Crimes Violentos Letais Intencionais é: {limite_superior_cvli}.")
print(f"\nLimite Inferior sobre Crimes Violentos Letais Intencionais é: {limite_inferior_cvli}.")
print(f'\nA distancia entre a Variância e Média sobre Crimes Violentos Letais Intencionais é {distancia__var_cvli:.2f}%.')
print(f'\nCoeficiente de Variação sobre Crimes Violentos Letais Intencionais é {coeficiente_var_cvli:.2f}%.')

print("\nVerificando Outliers")

if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print("\n--- Outliers Superiores ---")
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados sobre as recuperações de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Crimes Violentos Letais Intencionais no Rio de Janeiro')

if len(df_cvli_outliers_superiores) != 0 or len(df_cvli_outliers_inferiores) != 0:
    # Posição 01: Gráfico sobre Crimes Violentos Letais Intencionais
    plt.subplot(2,2,1)
    plt.title('BoxPlot sobre Crimes Violentos Letais Intencionais')
    plt.boxplot(array_cvli,vert=False,showmeans=True)

    # Posição 02: Histograma sobre Crimes Violentos Letais Intencionais
    plt.subplot(2,2,2)
    plt.title('Histograma dsobre Crimes Violentos Letais Intencionais')
    plt.hist(array_cvli,bins=100,edgecolor='black')

    # Posição 03: Crimes Violentos Letais Intencionais com Outliers
    df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
    plt.subplot(2,2,3)
    plt.title('Ranking sobre Crimes Violentos Letais Intencionais')
    plt.barh(df_cvli_outliers_superiores_order['aisp'],df_cvli_outliers_superiores_order['cvli'])

    # Posição 04: Medidas Descritivas sobre Crimes Violentos Letais Intencionais
    plt.subplot(2,2,4)
    plt.title('Medidas Descritivas sobre Crimes Violentos Letais Intencionais')
    plt.axis('off')
    plt.text(0.1,0.9,f"A média sobre Crimes Violentos Letais Intencionais é {media_cvli:.2f}.",fontsize=12)
    plt.text(0.1,0.8,f"A mediana sobre Crimes Violentos Letais Intencionais é {mediana_cvli}.",fontsize=12)
    plt.text(0.1,0.7,f"A distância entre a média e a mediana é {distancia:.2f}%",fontsize=12)
    plt.text(0.1,0.6,f"O maior número de casos: {maior_cvli}.",fontsize=12)
    plt.text(0.1,0.5,f'O menor número de casos: {menor_cvli}.',fontsize=12)
    plt.text(0.1,0.4,f'A distancia entre a Variância e Média sobre Crimes Violentos Letais Intencionais é {distancia__var_cvli:.2f}%.',fontsize=12)
    plt.text(0.1,0.3,f'Coeficiente de Variação sobre Crimes Violentos Letais Intencionais é {coeficiente_var_cvli:.2f}%.',fontsize=12)

else:
    # Posição 01: Gráfico sobre Crimes Violentos Letais Intencionais
    df_cvli_outliers_superiores_order = df_cvli_1.sort_values(by='cvli',ascending=True)
    plt.subplot(2,2,1)
    plt.title('Acumulado sobre Crimes Violentos Letais Intencionais')
    plt.bar(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'])

    # Posição 02: Histograma sobre Crimes Violentos Letais Intencionais
    plt.subplot(2,2,2)
    plt.title('Histograma sobre Crimes Violentos Letais Intencionais')
    plt.hist(array_cvli,bins=100,edgecolor='black')

    # Posição 03: Medidas Descritivas sobre Crimes Violentos Letais Intencionais
    plt.subplot(2,2,3)
    plt.title('Medidas Descritivas sobre Crimes Violentos Letais Intencionais')
    plt.axis('off')
    plt.text(0.1,0.9,f"A média sobre Crimes Violentos Letais Intencionais é {media_cvli:.2f}.",fontsize=12)
    plt.text(0.1,0.8,f"A mediana sobre Crimes Violentos Letais Intencionais é {mediana_cvli}.",fontsize=12)
    plt.text(0.1,0.7,f"A distância entre a média e a mediana é {distancia:.2f}%",fontsize=12)
    plt.text(0.1,0.6,f"O maior número de casos: {maior_cvli}.",fontsize=12)
    plt.text(0.1,0.5,f'O menor número de casos: {menor_cvli}.',fontsize=12)
    plt.text(0.1,0.4,f'A distancia entre a Variância e Média sobre Crimes Violentos Letais Intencionais é {distancia__var_cvli:.2f}%.',fontsize=12)
    plt.text(0.1,0.3,f'Coeficiente de Variação sobre Crimes Violentos Letais Intencionais é {coeficiente_var_cvli:.2f}%.',fontsize=12)


    # Posição 04: Vazio
    plt.subplot(2,2,4)
    plt.axis('off')

# Exibindo o Painel
plt.tight_layout()
plt.show()