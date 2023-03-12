from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f"{n}", end=' ', flush=True)
        sleep(0.3)
    print("PRONTO!")


def somapar(lista):
    par = 0
    for num in lista:
        if num % 2 == 0:
            par = par + num
    print(f"Somando os valores pares da {lista}, temos {par}")


numeros = []
sorteia(numeros)
somapar(numeros)
