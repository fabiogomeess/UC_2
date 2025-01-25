import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Lesões Corporais Dolosas 
df_lesoes = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_lesoes[['aisp','ano','lesao_corp_dolosa']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa['ano'].isin([2022,2023,2024])]
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['aisp']).sum(['lesao_corp_dolosa']).reset_index()

# Criando o DataFrame Lesões Corporais Culposas
df_lesao_corp_culposa = df_lesoes[['aisp','ano','lesao_corp_culposa']]
df_lesao_corp_culposa = df_lesao_corp_culposa[df_lesao_corp_culposa['ano'].isin([2022,2023,2024])]
df_lesao_corp_culposa = df_lesao_corp_culposa.groupby(['aisp']).sum(['lesao_corp_culposa']).reset_index()

# Exibindo a base de dados Lesões Corporais Dolosas 
print('\n---- EXIBINDO A BASE DE DADOS LESÕES CORPORAIS DOLOSAS -----')
print(df_lesao_corp_dolosa)

# Exibindo a base de dados Lesões Corporais Culposas
print('\n---- EXIBINDO A BASE DE DADOS LESÕES CORPORAIS CULPOSAS -----')
print(df_lesao_corp_culposa)

# Criando uma array Lesões Corporais Dolosas 
array_lesao_corp_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média Lesões Corporais Dolosas 
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)

# Obtendo a mediana Lesões Corporais Dolosas 
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)

# Obtendo a distância entre a média e a mediana Lesões Corporais Dolosas 
distancia_lesao_corp_dolosa = abs((media_lesao_corp_dolosa - mediana_lesao_corp_dolosa) / mediana_lesao_corp_dolosa) * 100

# Obtendo o máximo e o mínimo Lesões Corporais Dolosas 
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Obtendo a amplitude Lesões Corporais Dolosas 
amplitude_lesao_corp_dolosa = maximo_lesao_corp_dolosa - minimo_lesao_corp_dolosa

# Obtendo os Quartis Lesões Corporais Dolosas  - Método weibull
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25, method='weibull')
q2_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.50, method='weibull')
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75, method='weibull')
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa

# Identificando os outliers superiores e inferiores Lesões Corporais Dolosas 
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)
limite_inferior_lesao_corp_dolosa = q1_lesao_corp_dolosa - (1.5 * iqr_lesao_corp_dolosa)

# Filtrando o DataFrame Lesões Corporais Dolosas 
df_lesao_corp_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
df_lesao_corp_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_corp_dolosa]

# Obtendo as medidas de dispersão Lesões Corporais Dolosas 
variancia_lesao_corp_dolosa = np.var(array_lesao_corp_dolosa)
distancia_lesao_corp_dolosa = variancia_lesao_corp_dolosa / (media_lesao_corp_dolosa**2)
desvio_padrao_lesao_corp_dolosa = np.std(array_lesao_corp_dolosa)
coeficiente_var_lesao_corp_dolosa = desvio_padrao_lesao_corp_dolosa / media_lesao_corp_dolosa

# Obtendo a correlação entre as recuperações e os roubos de veículos
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação
correl_lesao_corp_dolosa = np.corrcoef(df_lesao_corp_dolosa['lesão_corp_dolosa'],df_lesao_corp_dolosa['lesão_corp_culposa'])[0,1]

# Exibindo os dados sobre as recuperações de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS DOLOSAS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das Lesões Corporais Dolosas  é {media_lesao_corp_dolosa:.0f}")
print(f"A mediana das Lesões Corporais Dolosas  é {mediana_lesao_corp_dolosa:.0f}")
print(f"A distância entre a média e a mediana das Lesões Corporais Dolosas  é {distancia_lesao_corp_dolosa:.2f} %")
print(f"O menor valor das Lesões Corporais Dolosas é {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor das Lesões Corporais Dolosas é {maximo_lesao_corp_dolosa:.0f}")
print(f"A amplitude dos valores das Lesões Corporais Dolosas é {amplitude_lesao_corp_dolosa:.0f}")
print(f"O valor do q1 - 25% das Lesões Corporais Dolosas é {q1_lesao_corp_dolosa:.0f}")
print(f"O valor do q2 - 50% das Lesões Corporais Dolosas é {q2_lesao_corp_dolosa:.0f}")
print(f"O valor do q3 - 75% das Lesões Corporais Dolosas é {q3_lesao_corp_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 das Lesões Corporais Dolosas é {iqr_lesao_corp_dolosa:.0f}")
print(f"O limite inferior das Lesões Corporais Dolosas é {limite_inferior_lesao_corp_dolosa:.0f}")
print(f"O limite superior das Lesões Corporais Dolosas é {limite_superior_lesao_corp_dolosa:.0f}")
print(f"A variância das Lesões Corporais Dolosas é {variancia_lesao_corp_dolosa:.0f}")
print(f"A distância da variância X média das Lesões Corporais Dolosas é {distancia_lesao_corp_dolosa:.0f}")
print(f"O desvio padrão das Lesões Corporais Dolosas é {desvio_padrao_lesao_corp_dolosa:.0f}")
print(f"O coeficiente de variação das Lesões Corporais Dolosas é {coeficiente_var_lesao_corp_dolosa:.0f}")
print(f"A correlação entre as Lesões Corporais Dolosas e Lesões Corporais Culposas é {correl_lesao_corp_dolosa:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesao_corp_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_corp_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_corp_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesao_corp_dolosa_outliers_superiores)