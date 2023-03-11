from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("Sua opções: ")
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print('-=' * 11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print('-=' * 11)
if computador == 0:  # PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("Parabéns!, Você Venceu")
    elif jogador == 2:
        print("Você perdeu, Tente Novamente")
    else:
        print("JOGADA INVÁLIDA")

elif computador == 1:  # PAPEL
    if jogador == 0:
        print("Você perdeu, Tente Novamente")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("Parabéns!, Você Venceu")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2:  # TESOURA
    if jogador == 0:
        print("Parabéns!, Você Venceu")
    elif jogador == 1:
        print("Você perdeu, Tente Novamente")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA")
