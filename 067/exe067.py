while True:
    m = int(input("Quer ver a tabuada de qual valor: "))
    if m < 0:
        break
    print("~~"*30)
    for n in range(1, 11):
        print(f"{m} x {n:2} = {m * n}")
    print("~~" * 30)
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")
