velocidade = float(input("Qual é a velocidade do carro? "))
if velocidade >= 81:
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    print(f"Você deve pagar uma multa de R${(velocidade-80)*7:.2f}")
print("Tenha um bom dia! Dirija com segurança")
