# Roubos e furtos # Exercicio: responder as perguntar utlizando as somas dos totais das Séries
import pandas as pd
def formatar(valor): #criação da função com objetivo de formatar um numero com duas casas decimais, usando FORMAT
    return "{:.2f}%".format(valor)
roubo_de_automoveis = pd.Series([100,90,80,120,110,90,70])
furto_de_automoveis = pd.Series([80,60,70,60,100,50,30])
recuperacao_de_automoveis = pd.Series([70,50,60,80,100,70,50])

print(f"A soma dos roubos dos últimos 7 dias é: {sum(roubo_de_automoveis)}")
print(f"\nA soma dos furtos dos últimos 7 dias é: {sum(furto_de_automoveis)}")
print(f"\nA soma da recuperação de veículos dos últimos 7 dias é: {sum(recuperacao_de_automoveis)}")
print(f"\nA soma dos roubos e furtos de veículos nos últimos 7 dias é: {(roubo_de_automoveis.sum() + furto_de_automoveis.sum())}")
total_tx_rec = (recuperacao_de_automoveis.sum() / roubo_de_automoveis.sum() * 100)
print(f"\nA porcentagem de veículos roubados recuperados nos últimos 7 dias é: {total_tx_rec:.2f}%")

