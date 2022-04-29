# A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um algoritmo que calcule e exiba o salário do professor. Sabe-se que o valor da hora/aula segue a tabela abaixo:

cont = 1
while (cont <= 50):
    nome = input("Nome do professor:")
    nivel = int(input("Nivel do professor de 1 a 3:"))
    horasT = float(input("Horas trabalhadas:"))

    if (nivel == 1):
        salario = horasT * 12.00
    elif (nivel == 2):
        salario = horasT * 17.00
    elif (nivel == 3):
        salario = horasT * 25.00
    else:
        print("Nivel não encontrado!")

    print("O professor", nome, "vai receber:", salario, "esse mes")

