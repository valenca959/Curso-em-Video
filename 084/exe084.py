banco = []
dados = []
mai = men = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    if len(banco) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    banco.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in "SsNn":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp in "Nn":
        break
print(f"Ao todo, você cadastrou {len(banco)} pessoas.")
print(f"O maior peso foi de {mai}Kg. Peso de ", end=' ')
for p in banco:
    if p[1] == mai:
        print(f"{p[0]}", end=' ')
print()
print(f"O menor peso foi de {men}Kg. peso de ", end=' ')
for p in banco:
    if p[1] == men:
        print(f"{p[0]}", end=' ')
print()
