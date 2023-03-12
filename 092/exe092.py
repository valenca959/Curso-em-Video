from datetime import date
ano = date.today().year
pessoa = dict()
pessoa["nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
pessoa['idade'] = ano - nasc
pessoa['ctps'] = int(input("Carteira de trabalho (0 se não tem): "))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input("Salário: R$"))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - ano)
print("-=" * 30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
