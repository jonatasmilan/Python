# Faça um Programa que leia três números e mostre-os em ordem decrescente.
a = float(input('Insira um número: '))
b = float(input('Insira um número: '))
c = float(input('Insira um número: '))

lista = [a, b, c]
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

lista.sort(reverse = True)  
# print(f'O maior número é o {maior}')
# print(f'O menor número é o {menor}')
print(lista)
