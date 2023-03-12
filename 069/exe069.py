pmais18 = homens = mmenos20 = 0
while True:
    print("--"*30)
    print("CADASTER UMA PESSOA")
    print("--" * 30)
    sexo = " "
    idade = int(input("Idade: "))
    cont = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        pmais18 = pmais18 + 1
    if sexo == "M":
        homens = homens + 1
    if idade < 20 and sexo in "F":
        mmenos20 = mmenos20 + 1
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {pmais18}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mmenos20} mulheres com menos de 20 anos")
