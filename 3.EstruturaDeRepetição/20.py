# Altere o programa de cálculo do fatorial, 
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    fatorial = int(input('Insira um número: '))
    if fatorial > 0 and fatorial < 16:
        resultado = 1
        print(f'{fatorial}!= ', end= '')
        for i in range(fatorial, 0, -1):
            resultado *= i
            print(f'{i}', '= ' if i == 1 else '. ', end='')
        print(resultado)
    else:
        print('Número inválido.')        
    check = input('Deseja continuar? [s] [n]')
    if check == 'n':     
        break
