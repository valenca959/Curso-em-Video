from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while not opcao == 5:
    opcao = int(input('''    [ 1 ] Somar 
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa
    >>>>>>>>>> Opção: '''))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} = {soma}")
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} = {multiplicar}")
    elif opcao == 3:
        maior = n1
        if n1 < n2:
            maior = n2
        print(f"Entre {n1} e {n2} o maior valor é {maior}")
    elif opcao == 4:
        print("Digite os valores novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, Tente novamente")
    print("=-="*10)
    sleep(1)
print("Fim do programa, Volte sempre!")
