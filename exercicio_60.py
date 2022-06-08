# ler um número e mostrar o seu fatorial

numero = int(input("Digite um número: "))

indice = numero

resultado = 1

while indice != 0:
    resultado = resultado * (indice)
    indice = indice - 1

print(resultado)