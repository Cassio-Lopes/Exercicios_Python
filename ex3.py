#Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 80, menor que 25 ou igual a 40. O usuário deverá informar se deseja continuar informando os valores.

resposta = True
resp = str
while (resposta == True):
    n = int(input("Digite um numero: "))
    if(n > 80):
        print("O numero Digitado é maior que 80")
    elif(n == 40):
        print("O numero Digitado é igual a 40")
    elif(n < 25):
        print("O numero Digitado é menor que 25")
    else:
        print("O numero Digitado foi: ", n)

    resp = input("Deseja continuar?(Sim/Não)")
    if(resp == "Não"):
        resposta = False