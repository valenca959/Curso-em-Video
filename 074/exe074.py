from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
maior = numeros[0]
menor = numeros[0]
print(f"{numeros}")
if numeros[1] > maior:
    maior = numeros[1]
    if numeros[2] > maior:
        maior = numeros[2]
        if numeros[3] > maior:
            maior = numeros[3]
            if numeros[4] > maior:
                maior = numeros[4]
                if numeros[5] > maior:
                    maior = numeros[5]
elif numeros[1] < menor:
    menor = numeros[1]
    if numeros[2] < menor:
        menor = numeros[2]
        if numeros[3] < menor:
            menor = numeros[3]
            if numeros[4] < menor:
                menor = numeros[4]
                if numeros[5] < menor:
                    menor = numeros[5]
print(f"O maior valor sorteado foi {maior}"
      f"\nO menor valor sorteado foi {menor}")
