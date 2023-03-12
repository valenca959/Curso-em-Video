from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = numeros[0]
menor = numeros[0]
print(f"Os valores sorteados foram: {numeros}")
for c in range(1, 5):
    if numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print(f"O maior valor sorteado foi {maior}"
      f"\nO menor valor sorteado foi {menor}")
