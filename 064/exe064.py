n = int(input("Digite um número[999 para parar]: "))
cont = 1
s = n
while n != 999:
    n = int(input("Digite um número[999 para parar]: "))
    if n != 999:
        cont = cont + 1
        s = s + n
print(f"Você digitou {cont} e a soma entre eles foi {s}.")
