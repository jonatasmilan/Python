# # Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.
    
int1 = int(input('Insira um número inteiro: '))
int2 = int(input('Insira um número inteiro: '))
real = float(input('Insira um número real: '))
print(f'A) {(2 * int1) * (int2 / 2)}')
print(f'B) {(3 * int1) + real}')
print(f'C) {(real ** 3):.2f}')
