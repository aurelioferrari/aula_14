# ler o numero e mostrar os n primeiros elementos da fibonacci

n = int(input("Quantos elementos você quer ver? "))
seq = [0, 1]
t1 = 0
t2 = 1
if n == 0:
    seq = []
if n == 1:
    seq = [0]
if n == 2:
    seq = [0, 1]
indice = 3
while indice <= n:
    t3 = t1 + t2
    seq.append(t3)
    t1 = t2
    t2 = t3
    indice += 1
print(seq)

