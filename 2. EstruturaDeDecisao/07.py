# Faça um Programa que leia três números e mostre o maior e o menor deles.
a = float(input('Insira um número: '))
b = float(input('Insira um número: '))
c = float(input('Insira um número: '))

maior = a
menor = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')