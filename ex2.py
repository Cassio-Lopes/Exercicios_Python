#Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.

n = int(input("Informe o numero de pessoas:"))
cont = 1
tAptos = 0
while cont <= n:
    nome = input("Informe o nome:")
    sexo = input("Informe o sexo (m/f):")
    idade = int(input("Informe a idade:"))
    saude = input("Informe a saude dessa pessoa (Boa/Ruim):")
    cont += 1

    if(sexo == "m" and idade >= 18 and idade <= 45 and saude == "Boa"):
        print(nome, "esta apto para cumprir os serviços militares.")
        tAptos += 1
    else:
        print(nome, "não esta apto para cumprir os serviços militare.")

print("O total de pessoas aptas para cumprir o serviço militar é de", tAptos)