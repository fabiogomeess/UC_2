# Importando a Biclioteca #numpy.org
import pandas as pd 
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame Financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
# Criando um array Idade (age)
array_titanic_idade = np.array(df_titanic['Age'])
# Criando um array da Tarifa (fare)
array_titanic_tarifa = np.array(df_titanic['Fare'])

# Obtendo resultados solicitados quanto a Tarifa (fare)
media_fare = np.mean(array_titanic_tarifa)
mediana_fare = np.median(array_titanic_tarifa)
distancia_media_mediana_f = abs((media_fare - mediana_fare) / mediana_fare)
maior_fare = np.max(array_titanic_tarifa)
menor_fare = np.min(array_titanic_tarifa)
amplitude_fare = maior_fare - menor_fare
q1_fare = np.quantile(array_titanic_tarifa, 0.25, method='weibull')
q2_fare = np.quantile(array_titanic_tarifa, 0.50, method='weibull')
q3_fare = np.quantile(array_titanic_tarifa, 0.75, method='weibull')
iqr_fare = q3_fare - q1_fare
limite_superior_fare = q3_fare + (1.5 * iqr_fare)
limite_inferior_fare = q1_fare - (1.5 * iqr_fare)
df_funcionarios_outliers_inferiores_fare = df_titanic[df_titanic['Fare'] < limite_inferior_fare]
df_funcionarios_outliers_superiores_fare = df_titanic[df_titanic['Fare'] > limite_superior_fare]


# Obtendo resultados solicitados quanto a Idade (age)
media_age = np.mean(array_titanic_idade)
mediana_age = np.median(array_titanic_idade)
distancia_media_mediana_a = abs((media_age - mediana_age) / mediana_age)
maior_age = np.max(array_titanic_idade)
menor_age = np.min(array_titanic_idade)
amplitude_age= maior_age - menor_age
q1_age = np.quantile(array_titanic_idade, 0.25, method='weibull')
q2_age = np.quantile(array_titanic_idade, 0.50, method='weibull')
q3_age = np.quantile(array_titanic_idade, 0.75, method='weibull')
iqr_age = q3_age - q1_age
limite_superior_age = q3_age + (1.5 * iqr_age)
limite_inferior_age = q1_age - (1.5 * iqr_age)
df_funcionarios_outliers_inferiores_age = df_titanic[df_titanic['Age'] < limite_inferior_age]
df_funcionarios_outliers_superiores_age = df_titanic[df_titanic['Age'] > limite_superior_age]


# Exibindo a Tabela Titanic
print("--- TABELA TITANIC ---")
print(df_titanic)

# Exibindo resultados FARE
print("\n--- RESULTADO DAS TARIFAS ---")
print(f"A valor médio da tarifa paga é R$ {media_fare:.2f}.")
print(f"O valor da mediana da tarifa paga é R$ {mediana_fare:.2f}.")
print(f"A distância entre a média e a mediana da tarifa é {distancia_media_mediana_f:.2f}.")
print(f"A maior tarifa paga é R$ {maior_fare:.2f}, enquanto a menor é R$ {menor_fare:.2f}.")
print(f"A amplitude entre as tarifas é R$ {amplitude_fare}.")
print(f"\nO valor do quartil 1 é {q1_fare}.")
print(f"O valor do quartil 2 é {q2_fare}.")
print(f"O valor do quartil 3 é {q3_fare}.")
print(f"O valor do IQR é {iqr_fare}.")
print(f"O limite inferior é {limite_inferior_fare}.")
print(f"O limite superior é {limite_superior_fare}.")
print("\n--- Outliers Inferiores ---")
if len(df_funcionarios_outliers_inferiores_fare) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_fare)
print("\n--- Outliers Superiores ---")
if len(df_funcionarios_outliers_superiores_fare) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_fare)

# Exibindo resultados AGE
print("\n--- RESULTADO DAS IDADES ---")
print(f"A idade média é {media_age:.0f} anos.")
print(f"A mediana das idades é {mediana_age:.0f} anos.")
print(f"A distância entre a média e a mediana das idades é {distancia_media_mediana_a:.2f}.")
print(f"A maior idade é {maior_age} anos, enquanto a menor é {menor_age}.")
print(f"A amplitude entre as idades é {amplitude_age}.")
print(f"\nO valor do quartil 1 é {q1_age}.")
print(f"O valor do quartil 2 é {q2_age}.")
print(f"O valor do quartil 3 é {q3_age}.")
print(f"O valor do IQR é {iqr_age}.")
print(f"O limite inferior é {limite_inferior_age}.")
print(f"O limite superior é {limite_superior_age}.")
print("\n--- Outliers Inferiores ---")
if len(df_funcionarios_outliers_inferiores_age) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_age)
print("\n--- Outliers Superiores ---")
if len(df_funcionarios_outliers_superiores_age) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_age)