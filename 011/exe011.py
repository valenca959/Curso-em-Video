l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
area = float(l*a)
tinta = float(area/2)
print(f'A sua parede tem a dimensão de {l}m x {a}m e sua área é de {area}m²'
      f'\nPara pintar essa parede, você precisará de {tinta:.2f}L de tinta')
