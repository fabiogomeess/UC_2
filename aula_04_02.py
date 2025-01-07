# Importando Biblioteca Pandas
import pandas as pd

# Importando a Base de Dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Financeira
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando o DataFrame Homicídio Doloso por Munícipio
df_hom_doloso_munic = df_ocorrencias[['munic','hom_doloso']]

# Consolidando o DataFrame Homicídio Doloso por Município
df_hom_doloso_munic = df_hom_doloso_munic.groupby(['munic']).sum(['hom_doloso']).reset_index()

# Exibindo o DataFrame
print("\n Base de Dados - Geral")
print(df_ocorrencias.head())
print("\ Base de Dados - Município e Homicidio Doloso")
print(df_hom_doloso_munic.head(70))