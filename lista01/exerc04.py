meses = int(input("Digite os meses em que quer emagrecer: "))
kgs = int(input("Digite o total de kgs que quer perder: "))

for mes in range(meses):
    print("Mes", mes + 1,  "você irá perder", str(kgs/meses) + "KG")