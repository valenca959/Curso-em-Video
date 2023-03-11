print('{:=^40}'.format("LOJAS VALENCA"))
preco = float(input("Preço das compas: R$"))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual é a sua opção: "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Parcelar em quantas vezes? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS")
else:
    total = preco
    print("OPÇÃO INVÁLIDADE DE PAGAMENTO. TENTE NOVAMENTE")
print(f"Sua compra de R${preco:.2f} vai custa R${total:.2f} no final")
