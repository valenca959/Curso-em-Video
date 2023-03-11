soma = 0
cont = 0
for n in range(1, 7):
    c = int(input(f"Digite o {n}º valor: "))
    if c % 2 == 0:
        soma = soma + c
        cont = cont + 1
print(f"Você informou {cont} números pares "
      f"\nA soma entre os números pares foi {soma}")
