melhor_tempo=0
pior_tempo_nome=""
melhor_tempo_nome=""
pior_tempo=0
tempo_total=0
tempo_1215=0

for nadador in range(4):
    nome_nadador = input("Digite o nome do nadador: ")
    tempo_nadador = int(input("Digite o tempo do nadador: "))
    tempo_total += tempo_nadador

    print(melhor_tempo, " A ", tempo_nadador)

    if nadador == 0:
        melhor_tempo_nome = nome_nadador
        pior_tempo_nome = nome_nadador
        melhor_tempo=tempo_nadador
        pior_tempo=tempo_nadador

    if tempo_nadador < melhor_tempo:
        melhor_tempo_nome = nome_nadador
        melhor_tempo = tempo_nadador
    
    if tempo_nadador > pior_tempo:
        pior_tempo_nome = nome_nadador
        pior_tempo = tempo_nadador

    if tempo_nadador >= 12 and tempo_nadador <= 15:
        tempo_1215+=1


print("Nome do nadador com o melhor tempo ", melhor_tempo_nome)
print("Nome do nadador com o pior tempo ", pior_tempo_nome)
print("Tempo médio dos nadadores ", tempo_total/7)
print("Quantidade de atletas com o tempo entre 12s e 15s ", tempo_1215)
