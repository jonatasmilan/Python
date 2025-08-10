# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais números ele é divisível.

num = int(input ("Digite um numero inteiro: "))
div = 0
divisoes = []

for i in range(1, num + 1):
    if num % i == 0:
        div += 1
        divisoes.append(i)

if div == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo e é divisível por: {divisoes}')