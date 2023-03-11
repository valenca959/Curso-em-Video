salario = float(input("Qual é o salário do funcionário: "))
if salario <= 1250:
    aumento = (salario*15)/100
else:
    aumento = (salario*10)/100
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salario+aumento:.2f}")
print(f"Teve um aumento de R${aumento:.2f}!")