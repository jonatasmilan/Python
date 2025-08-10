# Faça um programa que calcule e mostre a média aritmética de N notas.

n = 0
notas = 0
while True:
  nota = float(input('Insira uma nota: '))
  n += 1
  notas += nota
  media = notas / n
  check = input('Deseja parar? ')
  if check in 'Ss':
    break
print(f'A média aritmédica das {n} notas é {media:.2f}')