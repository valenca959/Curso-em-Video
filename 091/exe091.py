from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
for n in range(1, 5):
    sleep(0.3)
    jogador[n] = randint(1, 6)
    print(f"O {n}° jogador tirou {jogador[n]}.")
print("<<<VALORES SORTEADOS>>>")
print("-=" * 15)
ranking = {}
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º Lugar: {v[0]}º Jogador com {v[1]}.')
    sleep(0.7)
