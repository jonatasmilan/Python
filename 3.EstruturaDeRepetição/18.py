# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = float(input('Insira um número: '))
lista = [n]

while True:
    n = float(input('Insira um número: '))
    check = input('Deseja continuar? [s] [n]')
    lista.append(n)
    if check == 'n':
        break

print(f'O maior valor é {max(lista)}, o menor é {min(lista)} e a soma é {sum(lista):.2f}')