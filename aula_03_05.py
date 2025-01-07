# Importando a Biclioteca
import pandas as pd 

# Criando a Tabela Ocorrências
ocorrencias = [
    ['Rio de Janeiro',6775561,35000],
    ['Niteroi',515317,2500],
    ['São Gonçalo',1091737,15000],
    ['Duque de Caxias',924624,12000],
    ['Nova Iguaçu',821128,10000],
    ['Belford Roxo',513118,9000],
    ['São João de Meriti',471906,8500],
    ['Petrópolis',306678,1000],
    ['Volta Redonda',273988,2000],
    ['Campos dos Goytacazes',507548,4000],
]

# Criando as Colunas da Tabela Vendedor
colunas = ['Cidade','População','Roubos a Pedestres']

# Criando o DataFrame Ocorrências
df_ocorrencias = pd.DataFrame(ocorrencias,columns=colunas)



#taxa de roubos
print("Tabela com Dados das Cidades")
print(df_ocorrencias)
