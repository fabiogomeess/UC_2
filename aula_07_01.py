# Importando a Biclioteca
import pandas as pd 
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Financeira.csv'

# Criando o DataFrame Financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1') # CHARSET
df_financeira_renda_emprestimo = df_financeira[['Id_cliente','Renda','Vlr_emprestado']]

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
# Criando um array Renda
array_financeira_renda = np.array(df_financeira['Renda'])
# Criando um array da Tarifa (fare)
array_financeira_vlr_emprestado = np.array(df_financeira['Vlr_emprestado'])

# Obtendo dados solicitados sobre a Renda
media_renda = np.mean(array_financeira_renda)
mediana_renda = np.median(array_financeira_renda)
maior_renda = np.max(array_financeira_renda)
menor_renda = np.min(array_financeira_vlr_emprestado)
distancia_media_mediana_renda = abs((media_renda - mediana_renda) / mediana_renda)
amplitude_renda = maior_renda - menor_renda
q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull')
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda
limite_superior_renda = q3_renda + (1.5 * iqr_renda)
limite_inferior_renda = q1_renda - (1.5 * iqr_renda)
df_funcionarios_outliers_inferiores_renda = df_financeira[df_financeira['Renda'] < limite_inferior_renda]
df_funcionarios_outliers_superiores_renda = df_financeira[df_financeira['Renda'] > limite_superior_renda]

# Obtendo dados solicitados sobre a Valor Emprestado
media_valor_emprestado = np.mean(array_financeira_vlr_emprestado)
mediana_valor_emprestado = np.median(array_financeira_vlr_emprestado)
maior_valor_emprestado= np.max(array_financeira_vlr_emprestado)
menor_valor_emprestado = np.min(array_financeira_vlr_emprestado)
distancia_media_mediana_vlr_emp = abs((media_valor_emprestado - mediana_valor_emprestado) / mediana_valor_emprestado)
amplitude_valor_emprestado = maior_valor_emprestado - menor_valor_emprestado
q1_valor_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.25, method='weibull') # Metódo Weibull
q2_valor_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.50, method='weibull')
q3_valor_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.75, method='weibull')
iqr_valor_emprestado = q3_valor_emprestado - q1_valor_emprestado
limite_superior_valor_emprestado = q3_valor_emprestado + (1.5 * iqr_valor_emprestado)
limite_inferior_valor_emprestado = q1_valor_emprestado - (1.5 * iqr_valor_emprestado)
df_funcionarios_outliers_inferiores_valor_emprestado = df_financeira[df_financeira['Vlr_emprestado'] < limite_inferior_valor_emprestado]
df_funcionarios_outliers_superiores_valor_emprestado = df_financeira[df_financeira['Vlr_emprestado'] > limite_superior_valor_emprestado]


# Exibindo o DataFrame
# Exibindo a Tabela Financeira
print("--- TABELA FINANCEIRA ---")
# Caso Precise apresentar toda a tabela (print(df_financeira))
print(df_financeira_renda_emprestimo)

# Exibindo resultados RENDA
print("\n--- RESULTADO DA RENDA ---")
print(f"A valor médio da renda é de {media_renda}.")
print(f"O valor da mediana da renda é de {mediana_renda}.")
print(f"A distância entre a média e a mediana da renda é de {distancia_media_mediana_renda}.")
print(f"A maior renda é de {maior_renda}, enquanto a menor é {menor_renda}.")
print(f"A amplitude entre as rendas é de {amplitude_renda}.")
print(f"\nO valor do quartil 1 é {q1_renda}.")
print(f"O valor do quartil 2 é {q2_renda}.")
print(f"O valor do quartil 3 é {q3_renda}.")
print(f"O valor do IQR é {iqr_renda}.")
print(f"O limite inferior é {limite_inferior_renda}.")
print(f"O limite superior é {limite_superior_renda}.")
print("\n--- Outliers Inferiores ---")
if len(df_funcionarios_outliers_inferiores_renda) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_renda)
print("\n--- Outliers Superiores ---")
if len(df_funcionarios_outliers_superiores_renda) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_renda)


  # Exibindo resultados VALOR EMPRESTADO
print("\n--- RESULTADO DO VALOR EMPRESTADO ---")
print(f"A valor médio do valor emprestado é de {media_valor_emprestado}.")
print(f"O valor da mediana do valor emprestado é de {mediana_valor_emprestado}.")
print(f"A distância entre a média e a mediana do valor emprestado é de {distancia_media_mediana_vlr_emp}.")
print(f"A maior valor emprestado é de {maior_valor_emprestado}, enquanto a menor é {menor_valor_emprestado}.")
print(f"A amplitude entre os valores emprestados é de {amplitude_valor_emprestado}.")
print(f"\nO valor do quartil 1 é {q1_valor_emprestado}.")
print(f"O valor do quartil 2 é {q2_valor_emprestado}.")
print(f"O valor do quartil 3 é {q3_valor_emprestado}.")
print(f"O valor do IQR é {iqr_valor_emprestado}.")
print(f"O limite inferior é {limite_inferior_valor_emprestado}.")
print(f"O limite superior é {limite_superior_valor_emprestado}.")
print("\n--- Outliers Inferiores ---")
if len(df_funcionarios_outliers_inferiores_valor_emprestado) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_valor_emprestado)
print("\n--- Outliers Superiores ---")
if len(df_funcionarios_outliers_superiores_valor_emprestado) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_valor_emprestado)