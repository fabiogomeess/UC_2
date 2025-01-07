# Importando a Biclioteca
import pandas as pd 

#Criando a Tabela Vendedor
vendedores = [
    ['Maria',800,700,1000,900,1200,600,600],
    ['João',900,500,1100,1000,900,500,700],
    ['Manuel',700,600,900,1200,900,700,400]
]

# Criando as Colunas da Tabela Vendedor
colunas = ['Nome','Janeiro','Fevereiro','Março','Abril','Mario','Junho','Julho']

# Criando o DataFrame Vendedores
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Exibindo o DataFrame
print(df_vendedores)

# Realizando os Cálculos
soma_janeiro = df_vendedores['Janeiro'].sum()
media_janeiro = df_vendedores['Janeiro'].mean()
maior_janeiro = df_vendedores['Janeiro'].max()
menor_janeiro = df_vendedores['Janeiro'].min()
nome_maior_janeiro = df_vendedores[df_vendedores['Janeiro'] == maior_janeiro]['Nome']

# Exibindo os Resultados
print(f"\nO total do mês de Janeiro foi: R${soma_janeiro:.2f}")
print(f"\nA média do mês de Janeiro foi: R${media_janeiro:.2f}")
print(f"\nO maior valor no mês de Janeiro foi: R${maior_janeiro:.2f}")
print(f"\nO menor valor no mês de Janeiro foi: R${menor_janeiro:.2f}")
print(f"O vendedor do mês é o/a {nome_maior_janeiro.values[0]}") # O Values[0] significa que não quer a posição em que a pessoa se encontra na tabela