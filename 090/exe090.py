aluno = dict()
aluno['nome'] = str(input("Digite um nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}:  "))
aluno['situação'] = ' '
if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] <= 6.9:
    aluno['situação'] = "Recuperação"
else:
    aluno['situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f' {k} é igual a {v}')
