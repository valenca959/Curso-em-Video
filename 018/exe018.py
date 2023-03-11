from math import radians, sin, tan, cos
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
coss = cos(radians(a))
tang = tan(radians(a))
print(f'O ângulo de {a} tem o SENO de {seno:.2f}')
print(f'O ângulo de {a} tem o COSSENO de {coss:.2f}')
print(f'O ângulo de {a} tem a TANGENTE de {tang:.2f}')
