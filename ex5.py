#Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os seguintes critérios:

quantidade = int(input("Informe quantos funcionarios: "))
cont = 1
fSalarial = 0
while (cont <= quantidade):
    nome = input("Informe o nome:")
    salario = float(input("Informe o salario: R$"))
    sMinimo = float(input("Informe o salario minimo: R$"))

    if(salario < sMinimo * 3):
        aumento = salario * 0.50
        salario += aumento
    elif(salario > sMinimo * 3 and salario < sMinimo * 10):
        aumento = salario * 0.20
        salario += aumento
    elif (salario > sMinimo * 10 and salario < sMinimo * 20):
        aumento = salario * 0.15
        salario += aumento
    else:
        aumento = salario * 0.10
        salario += aumento

    fSalarial += salario
    cont += 1

print(nome, "O seu salario foi reajustado para, R$", salario, "Com um aumento de, R$", aumento)
print("Folha de pagamento aumentou em R$", fSalarial)