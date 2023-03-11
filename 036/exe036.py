casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
prestação = casa / (anos * 12)
minimo = (salario * 30) / 100
print(f"Para casa uma casa de \033[1:33:40mR${casa:.2f}\033[m em \033[1:33:40m{anos}\033[m anos"
      f"\nA prestação será de \033[1:33:40mR${prestação:.2f}\033[m")
if prestação <= minimo:
    print("Empréstimo APROVADO")
else:
    print("Empréstimo NEGADO")
