#Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.

quantidade = int(input("Quantas repetiçoes?"))
cont = 1
while (cont <= quantidade):
    n = float(input("Informe um numero:"))
    if (n > 0):
        print("Positivo")
    elif(n < 0):
        print("Negativo")
    else:
        print("Zero")

    cont += 1