from random import randint
v = 0
print("-=-=" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=-=" * 30)
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "IP":
        tipo = str(input("PAR ou ÌMPAR? [P/I]")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total}", end='')
    print(" DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!\nVamos jogar novamente.")
        else:
            break
    if tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!\nVamos jogar novamente.")
        else:
            break
    v = v + 1
print(f"GAME OVER! Você venceu {v} vezes.")
