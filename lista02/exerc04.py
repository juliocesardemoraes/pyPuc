razao_social=""
valor_total=0
clientes=[]

num_clientes = int(input("Digite o numero de clientes existentes: "))

for num in range(num_clientes):
    razao_social = input("Digite a razão social do cliente: ")
    valor_total = int(input("Digite o valor total das compras: "))
    cliente = {'razao_social': razao_social, 'valor_total':valor_total}
    clientes.append(cliente)

clientes_ordenados = sorted(clientes, key=lambda x: x['valor_total'], reverse=True)    

print(clientes_ordenados)

