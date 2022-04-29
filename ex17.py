#Desenvolva um algoritmo que leia 10 valores e ao final exiba a quantidade de valores múltiplo de 5.



multiplosDeCinco = 0
while (cont <= 10):
    n1 = float(input(f"Informe o  numero: {cont}ª"))

    if (n1 % 5 == 0):
        multiplosDeCinco += 1


print("A quantidade de valores multiplos de 5 é:", multiplosDeCinco)