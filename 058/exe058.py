from random import randint
computador = randint(0, 10)
contador = 0
print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue advinhar qual foi?")
palpite = int(input("Qual é seu palpite? "))
while palpite != computador:
    if palpite < computador:
        palpite = int(input("Mais... Tente mais uma vez."))
    elif palpite > computador:
        palpite = int(input("Menos... Tente mais uma vez."))
    contador = contador + 1
print(f"Eu pensei no número {computador}")
print(f"Acertou com {contador} tentativas. Parabéns!")
