#Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os lados de um triângulo. Se for, informar qual o tipo de triângulo que eles formam: equilátero, isóscele ou escaleno. Propriedade: o comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.

cont = 1
while (cont <= 1):
    n1 = int(input("Informe o primeiro lado do triangulo:"))
    n2 = int(input("Informe o segundo lado do triangulo:"))
    n3 = int(input("Informe o terceiro lado do triangulo:"))

    if (n1 == n2 and n2 == n3):
        print("Triângulo Equilátero")
    elif (n1 == n2 and n2 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1):
        print("Triângulo Isóscele")
    else:
        print("Triângulo Escaleno")

    cont += 1