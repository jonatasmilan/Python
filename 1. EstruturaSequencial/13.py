# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Insira sua altura: '))
s = input('Sexo(h ou m): ')
if s == 'h':
    print(f'Peso ideal (h) = {(72.7 * h) - 58:.2f}')
else:
    print(f'Peso ideal (m) = {(62.1 * h) - 44.7:.2f}')