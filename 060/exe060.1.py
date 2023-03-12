n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
print(f"calculando {n}! =", end='')
for c in range(1, 6):
    print(f"{c}", end='')
    print(" x " if c > 0 else "=" , end='')
    f = f * c
    c = c - 1
print(f'{f}')
