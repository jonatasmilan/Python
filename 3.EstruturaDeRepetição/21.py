# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

number = int(input('Insira um número: '))
if is_prime(number):
    print(f"{number} é primo")
else:
    print(f"{number} não é primo")