# ler primeiro termo e razão de uma PA e mostrar os 10 primeiros termos

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