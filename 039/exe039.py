from datetime import date
nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - nascimento
print(f"Quem nasceu no ano {nascimento} tem {idade} anos")
if idade < 18:
    print(f"Ainda falta {18 - idade} anos para o seu alistamento"
          f"\nSeu alistamento será em {nascimento + 18}.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
else:
    print(f"Voce já deveria ter se alistado há {idade - 18} anos"
          f"\nSeu alistamento foi em {nascimento + 18}")
