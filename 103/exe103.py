def ficha(jog='<desconhecido>', gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


nom = str(input("Nome do jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nom.strip() == '':
    ficha(gol=g)
else:
    ficha(nom, g)
