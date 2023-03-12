from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 0
while tot + 1 <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    sleep(0.8)
    print(f"{tot+1}° Jogo: {jogos[tot]}")
    tot += 1
