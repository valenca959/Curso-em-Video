lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Número adicionado ... ")
    else:
        print("Número duplicado, Não foi adicionado ...")
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp in "N":
        break
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista.")
