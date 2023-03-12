def area(larg,comp ):
    a = larg * comp
    print(f"A área de um terreno {larg} x {comp} e de {a}m²")


# Programa principal
print("Controle de Terrenos")
print("--" * 10)
l=float(input("LARGURA (m): "))
c=float(input("COMPRIMENTO (m): "))
area(l, c)
