# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
a = float(input('Insira um valor: '))
b = float(input('Insira um valor: '))
c = float(input('Insira um valor: '))

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
    
print(f'O produto mais barato é o {menor}')