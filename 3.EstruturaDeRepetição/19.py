# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
lista = []

while True:
    n = float(input('Insira um número: '))
    if n > 0 and n < 1000:
        lista.append(n)
    else:
        print('Número inválido.')
    check = input('Deseja continuar? [s] [n]')
    if check == 'n':
        break

print(f'O maior valor é {max(lista)}, o menor é {min(lista)} e a soma é {sum(lista):.2f}')