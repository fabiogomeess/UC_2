# Código usando séries
import pandas as pd
media = pd.Series([80,90,100,10,20,70,50,65,15,95]) # Criação de uma serie e armazenando ela em pd.Series
ap = media[media >= 70]
rp = media[media < 70]
print("--- Notas Maiores que 70 ---")
print(ap)
print("\n--- Notas Menores que 70 ---") # O "\n" ele salta a linha (retorno de ....)
print(rp)