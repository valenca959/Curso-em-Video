from time import sleep
def contador(*num):
    cont = maior = 0
    print("-=" * 30)
    print("ANALISANDO OS VALORES ...")
    tamanho = len(num)
    maior = 0
    for valor in num:
        print(f"{valor}", end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f'O maior valor informado foi {maior}. ')


#Programa principal
contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador(0)
