def soma_imposto( taxa_imposto, cust):
    return (1 + taxa_imposto/100)*cust


taxa_imposto = 10
res = 1

while res:
    if res:
        custo = float(input('Qual o custo do produto:'))
        print('O valor do produto é de', soma_imposto(taxa_imposto, custo))

    res =  int(input("Digite 0 se encerrar ouqualquer outro número para continuar:"))