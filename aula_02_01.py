# Código usando listas
media = [80,90,100,10,20,70,50,65,15,95]
ap = []
rp = [] 
for i in range(len(media)): # o "len" é para leitura da lista
    if media [i] >= 70:
        ap.append(media[i])
    else:
        rp.append(media[i])
print("--- Notas Maiores que 70 ---")
print(ap)
print("\n--- Notas Menores que 70 ---") # O "\n" ele salta a linha (retorno de ....)
print(rp)