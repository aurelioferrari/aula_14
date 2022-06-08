# digitar vários números e dizer quantos números são pares e quantos são ímpares

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        if n % 2 != 0:
            impar += 1
print("Pares: {} ímpares: {}".format(par, impar))