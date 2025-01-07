# Vendedores
import pandas as pd 
maria = pd.Series([800,700,1000,900,1200,600,600])
joão = pd.Series([900,500,1100,1000,900,500,700])
manuel = pd.Series([700,600,900,1200,900,700,400])

print("-------- Dados da vendedora Maria --------")
print(f"\nO total de vendas da Maria nos últimos 7 dias foi de R${maria.sum():.2f}, a média foi de R${maria.mean():.2f}, o maior valor foi de R${maria.max():.2f} e o menor valor foi de R${maria.min():.2f}.")
print("\n-------- Dados do vendedor João --------")
print(f"\nO total de vendas do João nos últimos 7 dias foi de R${joão.sum():.2f}, a média foi de R${joão.mean():.2f}, o maior valor foi de R${joão.max():.2f} e o menor valor foi de R${joão.min():.2f}.")
print("\n-------- Dados do vendedor Manuel --------")
print(f"\nO total de vendas da Manuel nos últimos 7 dias foi de R${manuel.sum():.2f}, a média foi de R${manuel.mean():.2f}, o maior valor foi de R${manuel.max():.2f} e o menor valor foi de R${manuel.min():.2f}.")