# Faça um Programa que leia três números e mostre o maior deles.
a = float(input('Insira um número: '))
b = float(input('Insira um número: '))
c = float(input('Insira um número: '))

if a > b and a > c:
    print(f'{a} é o maior número.')
if b > a and b > c:
    print(f'{b} é o maior número.')
if c > a and c > b:
    print(f'{c} é o maior número.')
else:
    print('Há números iguais.')