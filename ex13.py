Inicial = int(input("Informe o limite inicial:"))
Final = int(input("Informe o limite final:"))
par = 0
impar = 0
while (Inicial <= Final):
    resto = Inicial % 2

    if (resto == 0):
        par += 1
    else:
        impar += 1

    Inicial += 1

print("Pares:", par)
print("Impares", impar)