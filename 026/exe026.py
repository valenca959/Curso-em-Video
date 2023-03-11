fra = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {fra.count("A")} vezes na frase')
print(f'A primeira letra A apareceu na posição {fra.find("A")+1}')
print(f'A última letra A apareceu na posição {fra.rfind("A")+1}')
