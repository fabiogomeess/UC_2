# Código usando Séries para operações matemáticas
import pandas as pd
s1 = pd.Series([5,10,15,20,25,30,35,40,45,50])
s2 = pd.Series([5,2,3,4,25,6,7,8,9,10])
soma = s1 + s2 # Variável
print("A soma das Séries é:")
print(soma)
sub = s1 - s2 # Variável
print("\nA subtração das Séries é:")
print(sub)
multiplicacao = s1 * s2 # Variável
print("\nA multiplicação das Séries é:")
print(multiplicacao)
divisao = s1 / s2 # Variável
print("\nA divisão das Séries é:")
print(divisao)
