'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5 5! = 5 . 4 . 3 . 2 . 1 = 120'''

numero = int(input('Insira um número para calcular o fatorial: '))
total = 1
sequencia = []

for i in range(numero, 0, - 1):
    total *= i
    sequencia.append(str(i))
    

print(f"{numero}! = {' . '.join(sequencia)} = {total}")