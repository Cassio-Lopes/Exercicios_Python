#Faça um algoritmo que receba o nome a idade e o sexo de dez funcionário. Para cada funcionário mostre o nome e o salário líquido:

cont = 1
while (cont <= 10):
    salarioL = 0.0
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    sexo = input("Informe o sexo:(M/F)")

    if(sexo == "M"):
        if(idade >= 30):
            salarioL += 100.00
        else:
            salarioL += 50.00
    else:
        if (idade >= 30):
            salarioL += 200.00
        else:
            salarioL += 80.00

    print("Nome:", nome)
    print("Salario Liquido:", salarioL)

    cont += 1