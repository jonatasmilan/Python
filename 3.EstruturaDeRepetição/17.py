# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
# from math import factorial

# num = int(input('Insira um número: '))
# f = factorial(num)
# print(f'O fatorial de {num} é {f}')

# Usando estrutura de repetição

fatorial = int(input('Insira um número: '))
resultado = 1
print(f'{fatorial}!= ', end= '')
for i in range(fatorial, 0, -1):
    resultado *= i
    print(f'{i}', '= ' if i == 1 else '. ', end='')

print(resultado)

