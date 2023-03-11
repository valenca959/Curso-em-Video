from random import randint
from time import sleep
computador = randint(0, 5)#computador pensando
print('\033[0:33:40mVou pensar em um número entre 0 e 5, tente adivinhar...\033[m')
num = int(input("\033[7:37:40mEm que número eu pensei? \033[m"))#jogador pensando
print("\033[4:mPROCESSANDO...\033[m")
sleep(2)
if computador == num:
    print("\033[1:33mPARABÉNS! Você acertou.\033[m")
else:
    print(f"\033[1:33mGANHEI! Eu pensei no número {computador} e não no número {num}!\033[m")
