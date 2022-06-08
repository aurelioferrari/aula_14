# ler primeiro termo e razão de uma PA e mostrar os 10 primeiros termos
# perguntar se o usuario quer ver mais termos

primeiro = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão da PA?"))
pa = [primeiro]
indice = 2
n = primeiro
while indice < 11:
    n = n + razao
    pa.append(n)
    indice = indice + 1

print(pa)

opcao = str(input("Você quer ver mais elementos? [S / N]: ")).upper()
while opcao != "N" and opcao != "S":
    opcao = str(input("Você quer ver mais elementos? [S / N]: ")).upper()

while opcao == "S":
    adicionais = int(input("Quantos elementos você ainda quer ver? "))
    novo_indice = indice + adicionais
    while indice < novo_indice:
        n = n + razao
        pa.append(n)
        indice = indice + 1
    print("A Pa com os outros elementos é: {}".format(pa))
    opcao = str(input("Você quer ver mais elementos? [S / N]: ")).upper()
