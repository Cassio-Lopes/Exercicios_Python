#A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se o usuário deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.

cont = True
resp = str
vTotal = 0
while(cont == True):
    nomeC = input("Informe o nome do veiculo:")
    ano = int(input("Informe o ano do veiculo:"))
    valor = float(input("Informe o valor: R$"))

    if(ano <= 2000):
        valor -= valor * 0.12
        print("Valor com desconto: R$", valor)
    else:
        valor -= valor * 0.07
        print("Valor com desconto: R$", valor)

    vTotal += valor

    resp = input("Deseja continuar?(S/N)")
    if (resp == "N"):
        cont = False

print("Valor total: R$", vTotal)
