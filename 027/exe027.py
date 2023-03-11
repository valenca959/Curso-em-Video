nom = str(input('Digite seu nome completo: ')).strip()
nom = nom.split()
print(f'Seu primeiro nome é {nom[0]}')
print(f'Seu ultimo sobrenome é {nom[len(nom)-1]}')
