# Roubos e furtos
import pandas as pd
roubo_de_automoveis = pd.Series([100,90,80,120,110,90,70])
furto_de_automoveis = pd.Series([80,60,70,60,100,50,30])
recuperacao_de_automoveis = pd.Series([70,50,60,80,100,70,50])

print("A soma dos roubos dos últimos 7 dias é: ")
print(sum(roubo_de_automoveis))
print("\nA soma dos furtos dos últimos 7 dias é: ")
print(sum(furto_de_automoveis))
print("\nA soma da recuperação de veículos dos últimos 7 dias é: ")
print(sum(recuperacao_de_automoveis))
# Exercicio: responder as perguntar utlizando as somas dos totais das Séries

print("\nA quantidade de veículos furtados e roubados nos últimos 7 dias é:")
print((sum(roubo_de_automoveis)) + sum(furto_de_automoveis))

print("\nA porcentagem de veículos roubados recuperados nos últimos 7 dias é:")
porcentagem_rec  = ((sum(recuperacao_de_automoveis)) / sum(roubo_de_automoveis)) * 100
round_rec = round(porcentagem_rec, 2)
print(round_rec)
