#ler varios numeros e mostrar a media, o menor e o maior

n = int(input("Digite um número: "))
divisor = 1
media = n
lista = [n]
soma = n
pergunta = str(input("Você quer continuar? [S / N] ")).upper()
while pergunta in "Ss":
    n = int(input("Digite um número: "))
    lista.append(n)
    divisor += 1
    soma = soma + n
    pergunta = str(input("Você quer continuar? [S / N] ")).upper()
media = soma / divisor
lista.sort()

print(lista)

print("A média dos números digitados é: {}".format(media))
print("O maior número digitado é: {} e o menor é: {}".format(lista[divisor - 1], lista[0]))