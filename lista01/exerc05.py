nome = input("Digite os nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))

if(idade >=18):
    print(nome, "é maior de 18 anos e tem", idade,"anos")
else:
    print(nome, "é menor de 18 anos e tem", idade,"anos")
