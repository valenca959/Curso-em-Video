listagem = ("Borracha", 2, "Caderno", 15.90, "Estojo", 25, "Mochila", 120.32)
print('-' * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=' ')
    else:
        print(f"R${listagem[pos]:>6.2f}")
print('-' * 40)
