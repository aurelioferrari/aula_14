# pedir o sexo da pessoa. Se digitar uma opção inválida, pedir pra digitar novamente


sexo = str(input("Qual o seu sexo? [M / F / NB]: ")).upper()

while sexo != "M" and sexo != "F" and sexo != "NB":
    sexo = str(input("Qual o seu sexo? [M / F / NB]: ")).upper()

print("Obrigado.")
