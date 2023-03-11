peso = float(input("Qual o seu peso? (Kg)"))
altura = float(input("Qual é sua altura? (m)"))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Você está ABAIXO DO PESO ideal")
elif 18.5 <= imc < 25:
    print("Parabéns, Você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está com um SOBREPESO")
elif 30 <= imc < 40:
    print("CUIDADO!, Você esta com Obesidade")
else:
    print("Você está com OBESIDADE MÒRBIDA, Muito cuidado!!!!")
