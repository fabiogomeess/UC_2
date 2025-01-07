# Relatório de Vacinação COVID 4 anos
import pandas as pd

# Definindo a função para formatar
def formatar(valor): #criação da função com objetivo de formatar um numero com duas casas decimais, usando FORMAT
    return "{:.2f}%".format(valor)

população_vacinada = pd.Series([30000000, 25000000, 10000000, 5000000])
população_total = pd.Series([213317639, 214477744, 215574303, 216687971])

# CRIANDO AS VISUALIZAÇÕES
print("------- Dados de Vacinação -------")
print(f"\nO total da população vacinada é de {população_vacinada.sum()}, enquanto a média da população vacinada é de {população_vacinada.mean()}")
print("\n------- Dados da População -------")
print(f"\nO total da população do Brasil é de {população_total.sum()}, enquanto a média da população é de {população_total.mean()}")
print("\n------- Dados da Taxa de Vacinação -------")
tx_vac_anual = ((população_vacinada / população_total) * 100).apply(formatar)
print(f"\nA taxa dos últimos 4 anos é de:")
print(tx_vac_anual)
tx_vac = (população_vacinada.sum() / população_total.sum()) * 100
print(f"\nA taxa de vacinação anual, dos últimos 4 anos, é de {tx_vac:.2f}%")