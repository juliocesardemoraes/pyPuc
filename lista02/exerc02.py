idade = 0
maior_menor_idade = [0,0]
contador = 0

while idade >=0:
    idade = int(input("Digite a idade do aluno: "))

    if idade <0:
        break
    
    if contador == 0:
        maior_menor_idade[0] = idade
        maior_menor_idade[1] = idade
        contador+=1

    if idade < maior_menor_idade[0]:
        maior_menor_idade[0] = idade

    if idade > maior_menor_idade[1]:
        maior_menor_idade[1] = idade


print(maior_menor_idade)

print("Media entre a maior e menor idade ", (maior_menor_idade[0] + maior_menor_idade[1]) / 2)



