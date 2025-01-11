# Importando a Biclioteca #numpy.org
import pandas as pd 
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame Financeira
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Criando um array (lista) do Salário
array_funcionarios_salario = np.array(df_funcionarios['Salário'])
# Criando um array da Idade
array_funcionarios_idade = np.array(df_funcionarios['Idade'])
# Criando um array do Tempo de Empresa
array_funcionarios_tempo = np.array(df_funcionarios['Tempo'])

# Obtendo os resultados solicitados
media_salarial = np.mean(array_funcionarios_salario)
maior_salario = np.max(array_funcionarios_salario)
menor_salario = np.min(array_funcionarios_salario)
amplitude_salario = maior_salario - menor_salario
mediana_salarial = np.median(array_funcionarios_salario)
distancia_salario = abs((media_salarial - mediana_salarial) / mediana_salarial)


media_idade = np.mean(array_funcionarios_idade)
maior_idade = np.max(array_funcionarios_idade)
menor_idade = np.min(array_funcionarios_idade)
amplitude_idade = maior_idade - menor_idade
mediana_idade = np.median(array_funcionarios_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade)


maior_tempo = np.max(array_funcionarios_tempo)
menor_tempo = np.min(array_funcionarios_tempo)
amplitude_tempo = maior_tempo - menor_tempo # Diferença entre o maior e o menor
media_tempo = np.mean(array_funcionarios_tempo)
mediana_tempo = np.median(array_funcionarios_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo) / mediana_tempo)

qtd_funcionarios = np.count_nonzero(array_funcionarios_idade)
func_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
func_antigo = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']

# Exibindo o DataFrame Funcionários
print("------ Tabela Funcionários ------")
print(df_funcionarios)

# Exibindo os resultados solicitados
print("\n--- Resultados das Idades ---")
print(f"A media de idade dos funcionários da empresa é {media_idade:.0f} anos.")
print(f"A mediana de idade dos funcionários da empresa é {mediana_idade:.0f} anos.")
print(f"A Distância entre a média e a mediana é de {distancia_idade:2f}.")
print(f"A amplitude das idades dos funcionários da empresa é de {amplitude_idade:.0f} anos.")
print(f"O funcionário mais novo da empresa é o/a {func_novo.values[0]} com {menor_idade} anos, e o mais velho é o/a {func_antigo.values[0]} com {maior_idade} anos.")
print("\n--- Resultados dos Salários ---")
print(f"A média salarial da empresa é R$ {media_salarial:.2f}.")
print(f"A mediana salarial da empresa é R$ {mediana_salarial:.2f}.")
print(f"A Distância entre a média e a mediana é de {distancia_salario:.2f}.")
print(f"O maior salário da empresa é R$ {maior_salario:.2f}, enquanto o menor é R$ {menor_salario:.2f} e a amplitude entre eles (difenreça) é R$ {amplitude_salario:.2f}.")
print("\n--- Resultados do Tempo de Empresa ---")
print(f"O maior tempo na empresa é de {maior_tempo} anos, enquanto o menor tem {menor_tempo} anos e a amplitude (diferença entre eles) é de {amplitude_tempo} anos.")
print(f"A média do tempo de casa é de {media_tempo:.0f} anos.")
print(f"A mediana do tempo de casa é de {mediana_tempo:.0f} anos.")
print(f"A Distância entre a média e a mediana é de {distancia_tempo:.2f}.")
print(f"\nO total de funcionários da empresa é {qtd_funcionarios} pessoas.")