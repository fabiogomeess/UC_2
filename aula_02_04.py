# Roubos e furtos
import pandas as pd
def formatar(valor): #criação da função com objetivo de formatar um numero com duas casas decimais, usando FORMAT
    return "{:.2f}%".format(valor)
roubo_de_automoveis = pd.Series([100,90,80,120,110,90,70])
furto_de_automoveis = pd.Series([80,60,70,60,100,50,30])
recuperacao_de_automoveis = pd.Series([70,50,60,80,100,70,50])
roubo_mais_furto = roubo_de_automoveis + furto_de_automoveis 
print("A quantidade de roubos e furtos nos últimos 7 dias foi de:")
print(roubo_mais_furto)
tx_rec = ((recuperacao_de_automoveis / roubo_de_automoveis) * 100).apply(formatar)
print("O índice de recuperação é de:")
print(tx_rec)
print(sum(roubo_de_automoveis))
print(sum(furto_de_automoveis))
print(sum(recuperacao_de_automoveis))
# Exercicio: responder as perguntar utlizando as somas dos totais das Séries