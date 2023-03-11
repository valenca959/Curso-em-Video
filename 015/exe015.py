d = float(input('Informe o número de dias que foi alugado: '))
vd = d*60
km = float(input('informe a distancia percorrida em km: '))
vk = km*0.15
v = vd+vk
print(f'O valor pelo dias alugado foi de R${vd}\n'
      f'O valor pela distancia percorrida R${vk}\n'
      f'O total a pagar foi de R${v}')
