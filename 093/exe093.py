jogador = dict()
partida = list()
jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f'    Quantas partidas {jogador["nome"]} jogou? '))
for n in range(0, partidas):
    partida.append(int(input(f"Quantos gols na {n + 1}° partida ? ")))
print("-=" * 30)
jogador["gols"] = partida[:]
jogador['total'] = sum(partida)
print(jogador)
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas ")
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("-=" * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f"Foi um total de {jogador['total']} gols.")
