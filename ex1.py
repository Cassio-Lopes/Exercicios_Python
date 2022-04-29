# Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

cont = 1
contN = 0
while cont <= 80:
    n = int(input(f"Digite o  numero: {cont}º"))
    cont += 1
    if (n >= 10 and n <= 150):
        contN += 1
print("Ha", contN, "numeros entre o intervalo de 10 a 150!")