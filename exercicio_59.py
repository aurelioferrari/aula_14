# ler 2 valores e realizar opeações ou digitar uma opção pra sair

n1 = float(input("Qual o primeiro número? "))
n2 = float(input("Qual o segundo número? "))
resultado = 0
print(
    "[1] Somar\n"
    "[2] Multiplicar\n"
    "[3] Ver qual é o maior número\n"
    "[4] Digitar novos números\n"
    "[5] Sair do programa\n"
)
opcao = int(input("O que você quer fazer? "))
while opcao != 5:
    if opcao == 1:
        resultado = n1 + n2
        print("O resultado da soma é: {}".format(resultado))
    if opcao == 2:
        resultado = n1 * n2
        print("O resultado da multiplicação é: {}".format(resultado))
    if opcao == 3:
        if n1 > n2:
            print("O primeiro número é maior.")
        if n1 < n2:
            print("O segundo número é maior.")
    if opcao == 4:
        n1 = float(input("Qual o primeiro número? "))
        n2 = float(input("Qual o segundo número? "))

    print(
        "[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Ver qual é o maior número\n"
        "[4] Digitar novos números\n"
        "[5] Sair do programa\n"
    )
    opcao = int(input("O que você quer fazer? "))