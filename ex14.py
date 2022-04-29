#Dados três valores A, B e C, em que A e B são números reais e C é um caractere, pede-se para imprimir o resultado da operação de A por B se C for um símbolo de operador aritmético; caso contrário deve ser impressa uma mensagem de operador não definido. Tratar erro de divisão por zero. Repita esse processo cinco vezes.

cont = 1
while (cont <= 5):
    a = float(input("Informe o primerio valor:"))
    b = float(input("Informe o segundo valor:"))
    c = input("Informe o operador:")

    if (c == "+"):
        resutado = a + b
        print(a, "+", b, "=", resutado)
    elif (c == "-"):
        resutado = a - b
        print(a, "-", b, "=", resutado)
    elif (c == "*" or c == "x"):
        resutado = a * b
        print(a, "x", b, "=", resutado)
    elif (c == "/"):
        if(a == 0 or b == 0):
            print(a, "/", b, "= ∞")
        else:
            resutado = a / b
            print(a, "/", b, "=", resutado)
    else:
        print("operador não definido.")