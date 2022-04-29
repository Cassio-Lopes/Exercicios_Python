#Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe média de preço de custo e do preço de venda.

cont = 1
custo = 0
venda = 0
while(cont <= 40):
    saldo = 0
    nomeP = input("Nome do produto:")
    precoC = float(input("Preço de custo: R$"))
    precoV = float(input("Preço de venda: R$"))

    saldo -= precoC
    saldo += precoV

    custo += precoC
    venda += precoV

    if(saldo > 0):
        print("O produto gerou um lucro de: R$", saldo)
    elif(saldo < 0):
        print("O produto gerou um prejuizo de: R$", saldo)
    else:
        print("O produto ficou no", saldo)

    cont += 1

mediaC = custo / 2
mediaV = venda / 2
print("A media do preço de custo foi: R$",mediaC, "A media do preço de venda foi: R$", mediaV)