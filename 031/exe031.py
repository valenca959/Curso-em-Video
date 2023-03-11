viagem = float(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {viagem:.2f}Km.")
if viagem <= 200:
   preço = viagem * 0.50
else:
   preço = viagem * 0.45
print(f"E o preço da sua passagem será de {preço}")
