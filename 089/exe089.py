notas = []
lista = []
while True:
    resp = ' '
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Nota 1: ")))
    lista.append(float(input("Nota 2: ")))
    lista.append((lista[1]+lista[2])/2)
    notas.append(lista[:])
    lista.clear()
    while resp not in "SsNn":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
    print("~"*30)
for c in range(0, len(notas)):
    print(f"{c:.<2}", end=' ')
    print(f"{notas[c][0]:<10}", end=' ')
    print(f"{notas[c][3]:>5}")

while True:
    opc = int(input("Mostrar notas de qual aluno ?[999 finaliza]: "))
    print(f'{notas[opc]}')
    if opc == 999:
        break
print('<<< VOLTE SEMPRE >>>')
