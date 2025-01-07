# Importando a Biclioteca
import pandas as pd 

# Criando a Tabela Vendedor
vendedores = [
    ['Ana','F',28,120],
    ['Bruno','M',34,150],
    ['Carlos','M',45,110],
    ['Diana','F',30,95],
    ['Eduardo','M',40,130],
    ['Fernanda','F',29,140],
    ['Gustavo','M',38,105],
    ['Helena','F',31,125],
    ['Igor','M',27,100],
    ['Juliana','F',33,135],
]

# Criando as Colunas da Tabela Vendedor
colunas = ['Nome','Sexo','Idade','Vendas']

# Criando o DataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Realizando os Cálculos
soma_vendas = df_vendedores['Vendas'].sum()
media_vendas = df_vendedores['Vendas'].mean()
media_idades = df_vendedores['Idade'].mean()
maior_idade = df_vendedores['Idade'].max()
menor_idade = df_vendedores['Idade'].min()

# Maior e Menor Vendedores
maior_vendas = df_vendedores['Vendas'].max()
menor_vendas = df_vendedores['Vendas'].min()
nome_maior_vendas = df_vendedores[df_vendedores['Vendas'] == maior_vendas]['Nome']
nome_menor_vendas = df_vendedores[df_vendedores['Vendas'] == menor_vendas]['Nome']

# Quantidade de Vendas por Sexo
sexo_f = df_vendedores[df_vendedores['Sexo'] == 'F']['Vendas'].sum()
sexo_m = df_vendedores[df_vendedores['Sexo'] == 'M']['Vendas'].sum()


# Exibir o DataFrame (Exibindo Todos os Dados da Tabela)
print("\n --- Tabela Vendedores ---")
print(df_vendedores)

# Resultado dos Cálculos (Dados Solicitados)
print("\n --- Dados Solicitados ---")
print(f"A quantidade total de vendas foi {soma_vendas:.2f}.")
print(f"A quantidade média de vendas foi {media_vendas:.2f}.")
print(f"A maior idade é {media_idades}.")
print(f"A maior idade é {maior_idade}.")
print(f"A maior idade é {menor_idade}.")
print(f"O maior número de vendas foi de {maior_idade}.")
print(f"O menor número de vendas foi de {menor_idade}.")
print(f"O maior vendedor(a) foi {nome_maior_vendas.values[0]}, vendendo {maior_vendas}.")
print(f"O menor vendedor(a) foi {nome_menor_vendas.values[0]}, vendendo {menor_vendas}.")
print(f"O sexo feminino vendeu {sexo_f}, enquanto o sexo masculino vendeu, no mesmo período, {sexo_m}.")