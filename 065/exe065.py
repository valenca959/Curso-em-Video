maior = menor = cont = media = 0
resp = "S"
while resp in "Ss":
    num = int(input("Digite um número: "))
    media = media + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]")).strip()[0].upper()
print(f"Você digitou {cont} números e a média foi {media / cont}"
      f"\nO maior valor foi {maior} e o menor foi {menor}")
