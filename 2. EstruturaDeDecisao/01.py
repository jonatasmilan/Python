# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Insira um número: '))
num2 = float(input('Insira um número: '))

if num1 > num2:
    print(f'{num1:.2f} é o maior número inserido.')
elif num2 > num1:
    print(f'{num2:.2f} é o maior número inserido.')
else:
    print('Os números são iguais.')