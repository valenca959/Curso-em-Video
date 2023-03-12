lista = []
while True:
    resp = " "
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    while resp not in "SsNn":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "Nn":
        break
print("-="*30)
print(f'Você digitou os valores {sorted(lista)}')
