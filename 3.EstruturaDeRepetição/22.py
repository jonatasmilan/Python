# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

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