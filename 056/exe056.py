somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print(f"__________{p}° PESSOA__________")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexp [M/F]: ")).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher = totmulher + 1
media = somaidade / 4
print(f"A média de idade do grupo é de {media} anos.")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')
