temperaturas = []
temp_total=0
menor_temp = 0
maior_temp = 0
media_temp = 0
# First position is positive and the second one is negative
posneg_temp = [0,0]

for temp in range(5):
    temperatura_selecionada = int(input("Digite uma temperatura "))
    
    if temp == 0:
        menor_temp = temperatura_selecionada
        maior_temp = temperatura_selecionada
    
    temperaturas.append(temperatura_selecionada)

    if(temperatura_selecionada > 0):
        posneg_temp[0] += 1
    else:
        posneg_temp[1] += 1

    if temperatura_selecionada < menor_temp:
        menor_temp = temperatura_selecionada
    elif temperatura_selecionada > maior_temp:
        maior_temp = temperatura_selecionada

    temp_total+=temperatura_selecionada

print("A menor temperatura é ", menor_temp)
print("A média das temperaturas entre ",menor_temp," e ",maior_temp," é: ", temp_total/5)
print("São ", posneg_temp[1] ," temperaturas negativas e ", posneg_temp[0], " temperaturas positivas")
