print('-='*30)
print("Analisador de Triângulos!")
print('-='*30)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
