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

# Obtendo resultados solicitados quanto a Idade (age)
media_age = np.mean(array_titanic_idade)
mediana_age = np.median(array_titanic_idade)
distancia_media_mediana_a = abs((media_age - mediana_age) / mediana_age)
maior_age = np.max(array_titanic_idade)
menor_age = np.min(array_titanic_idade)
amplitude_age= maior_age - menor_age

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

# Exibindo resultados AGE
print("\n--- RESULTADO DAS IDADES ---")
print(f"A idade média é {media_age:.0f} anos.")
print(f"A mediana das idades é {mediana_age:.0f} anos.")
print(f"A distância entre a média e a mediana das idades é {distancia_media_mediana_a:.2f}.")
print(f"A maior idade é {maior_age} anos, enquanto a menor é {menor_age}.")
print(f"A amplitude entre as idades é {amplitude_age}.")

