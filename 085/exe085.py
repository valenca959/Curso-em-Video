banco = []
dados = []
for n in range(1, 8):
    dados.append(int(input(f"Digite o {n}° valor: ")))
    banco.append(dados[:])
    dados.clear()
banco.sort()
print("Os valores pares digitados foram :", end=' ')
for num in banco:
    if num[0] % 2 == 0:
        print(f'{num[0]}', end=' ')
print()
print("Os valores ímpares digitados foram:", end=' ')
for num in banco:
    if num[0] % 2 == 1:
        print(f"{num[0]}", end=' ')
print()
