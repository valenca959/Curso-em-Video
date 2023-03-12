total = p1000 = menor = cont = 0
barato = " "
print("---" * 30)
print("LOJA SUPER BARATÂO")
print("---" * 30)
while True:
    nompro = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    cont = cont + 1
    total = total + preco
    if preco >= 1000:
        p1000 = p1000 + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nompro
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {p1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
