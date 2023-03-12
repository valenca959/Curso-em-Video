time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantoas partidas o {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na na {c+1}° partida? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Por favor Responda com S ou N.")
    if resp == 'N':
        break

print("-=" * 30)
print("cod", end='')
for i in jogador.keys():
    print(f"{  i:<15}", end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15} ", end='')
    print()
print('-' * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? [999 para finalizar] "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No {i}° Jogo fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
