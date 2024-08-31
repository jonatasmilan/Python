# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.


num = int(input ("Digite um numero inteiro: "))
div = 0

for i in range(1, num + 1):
    if num % i == 0:
        div += 1

if div == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
        
