from datetime import date
ano = int(input("Ano de Nascimento: "))
idade = date.today().year - ano
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÙNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
