# o jogador precisa advinhar um número entre 0 e 10. Enquanto não acerta, ele tenta de novo.

import random


jogador = int(input("Em qual número eu estou pensando? "))
pc = random.randint(0, 10)
tentativas = 0
while jogador != pc:
    print("\033[1:31mVocê errou\033[m\n")
    tentativas += 1
    jogador = int(input("Em qual número eu estou pensando? "))
    pc = random.randint(0, 10)
else:
    print("Você acertou")
print("Você precisou de {} tentativas".format(tentativas))
