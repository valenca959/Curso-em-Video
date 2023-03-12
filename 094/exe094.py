lista = list()
dados = dict()
idade = 0
resp = ''
while True:
    dados['nome'] = str(input("Nome: "))
    dados['sexo'] = str(input("Sexo: [M/F]")).strip().upper()[0]
    while dados['sexo'] not in "MmFf":
        dados['sexo'] = str(input("ERRO! por favor, digite apenas M ou F: ")).strip().upper()[0]
    dados['idade'] = int(input("Idade: "))
    idade = idade + dados['idade']
    lista.append(dados.copy())
    resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    print("~~" * 30)
    while resp not in "SN":
        resp = str(input("ERRO! responda apenas S ou N: ")).strip().upper()[0]
    if resp in 'Nn':
        break
media = idade / len(lista)
print(f"Ao todo temos {len(lista)} pessoas cadastradas.")
print(f"A média de idade é de {media} anos.")
for p in lista:
    if p['sexo'] in "Ff":
        print(f"{p['nome']}.", end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}.', end=' ')
        print()
print('  <<<  ENCERRADO  >>>   ')
