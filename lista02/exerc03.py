from random import seed
from random import randint

seed(1)

escolha = ""
pessoas = []

while escolha !="S" or escolha !='s':
    print("Registre uma pessoa ou Digite S para fazer o sorteio")
    escolha = input("Digite o nome da pessoa para registrar na rifa ")

    if escolha == "S" or escolha =="s":
        break

    pessoas.append(escolha)

valor_escolhido = randint(0,len(pessoas))
print("O nome sorteado foi: ", pessoas[valor_escolhido])
