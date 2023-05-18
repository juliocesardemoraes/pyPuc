mes_selecionado = int(input("Digite um numero de um mes(EX: Janeiro(1)) "))
contador = 0
parimpar = "impar"

if mes_selecionado % 2 == 0:
    parimpar="par"

for mes in range(12):
    if mes_selecionado == mes :
        break
    contador+=mes

print("A soma dos valores menores que o mês atual é igual a " + str(contador))
print("O próximo mês é " + str(mes_selecionado + 1))
print("O mês atual é " + parimpar)
