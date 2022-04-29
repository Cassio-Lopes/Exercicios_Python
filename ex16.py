#Faça um algoritmo que calcule o valor da conta de luz de 30 pessoas. Sabe-se que o cálculo da conta de luz segue a tabela abaixo:

print("====================================")
print("|Tipo de Cliente		|Valor do KW/h|")
print("|1 (Residência)		|R$ 0,60      |")
print("|2 (Comércio)		|R$ 0,48      |")
print("|3 (Indústria)		|R$ 1,29      |")
print("====================================")

while (cont <= 30):
    Apagar = 0
    kWh = float(input("Informe os kW/h usados:"))
    tCliente = int(input("Informe o tipo de cliente:"))

    if(tCliente == 1):
        Apagar = kWh * 0.60
    elif (tCliente == 2):
        Apagar = kWh * 0.48
    elif (tCliente == 3):
        Apagar = kWh * 1.29
    else:
        print("Codigo invalido!")

    print("O valor a pagar sera R$", Apagar)