'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

intervalo_1 = []
intervalo_2 = []
intervalo_3 = []
intervalo_4 = []

while True:
  numero = float(input('Insira um número: '))
  if numero < 0:
    break
  if 0 < numero <= 25:
    intervalo_1.append(numero)
  if 26 < numero <= 50:
    intervalo_2.append(numero)
  if 51 < numero <= 75:
    intervalo_3.append(numero)
  if 76 < numero <= 100:
    intervalo_4.append(numero)
print(f'No intervalo de 0 a 25 existem {len(intervalo_1)} números')
print(f'No intervalo de 26 a 50 existem {len(intervalo_2)} números')
print(f'No intervalo de 51 a 75 existem {len(intervalo_3)} números')
print(f'No intervalo de 76 a 100 existem {len(intervalo_4)} números')