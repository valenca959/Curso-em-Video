from time import sleep


def contador(i, f, p):
    print("-=" * 20)
    print(f"Contagem de {i} até {f}, de {p} em {p} FIM!")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")


# Programa principal
contador(i=1, f=10, p=1)
print()
contador(i=10, f=0, p=2)
print()
print("-=" * 20)
print("Agora é sua vez")
ini = int(input('Início: '))
fim = int(input("Fim: "))
passo = int(input('Passo: '))
contador(i=ini, f=fim, p=passo)
