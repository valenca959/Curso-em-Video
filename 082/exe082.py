lista = []
impares = []
pares = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print("-="*30)
lista.sort()
print(f"A lista completa é {lista}")
pares.sort()
print(f"A lista de pares é {pares}")
impares.sort()
print(f"A lista de impares é {impares}")
