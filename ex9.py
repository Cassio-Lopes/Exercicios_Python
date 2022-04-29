#Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir apólices de seguro. Quanto às classes de ocupações, foram definidos três grupos de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco. Dados nome, idade e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a categoria do pretendente e caso a idade não esteja na faixa necessária, imprimir uma mensagem.

print("___________________________________________")
print("|               GRUPO DE RISCO            |")
print("|IDADE		|BAIXO		|MEDIO		|ALTO|")
print("|17 A 20		|1			|2			|3   |")
print("|21 A 24		|2			|3			|4   |")
print("|25 A 34		|3			|4			|5   |")
print("|35 A 64		|4			|5			|6   |")
print("|65 A 70		|7			|8			|9   |")
print("___________________________________________")

nome = input("Informe o nome:")
idade = int(input("Informe a idade:"))
gRisco =  int(input("Informe o grupo de rispo:"))

if(idade >= 17 and idade <= 20):
    if(gRisco == 1):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria baixa")
    elif(gRisco == 2):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria medio")
    elif(gRisco == 3):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria alto")
    else:
        print("Categoria não adequada para idade!")
elif(idade >= 21 and idade <= 24):
    if (gRisco == 2):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria baixa")
    elif (gRisco == 3):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria medio")
    elif (gRisco == 4):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria alto")
    else:
        print("Categoria não adequada para idade!")
elif(idade >= 25 and idade <= 34):
    if (gRisco == 3):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria baixa")
    elif (gRisco == 4):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria medio")
    elif (gRisco == 5):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria alto")
    else:
        print("Categoria não adequada para idade!")
elif(idade >= 35 and idade <= 64):
    if (gRisco == 4):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria baixa")
    elif (gRisco == 5):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria medio")
    elif (gRisco == 6):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria alto")
    else:
        print("Categoria não adequada para idade!")
elif(idade >= 65 and idade <= 70):
    if (gRisco == 7):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria baixa")
    elif (gRisco == 8):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria medio")
    elif (gRisco == 9):
        print("Nome:", nome)
        print("Idade:", idade)
        print("Categoria alto")
    else:
        print("Categoria não adequada para idade!")
else:
    print("Idade não esta na faixa que o seguro aceita!")