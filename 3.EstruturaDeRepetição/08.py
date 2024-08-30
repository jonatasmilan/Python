# Faça um programa que leia 5 números e informe a soma e a média dos números.
media = 0
soma = 0
for i in range(5):
    num = float(input('digite um número: '))
    soma += num
    media = soma / 5
print(f'média {media} e soma {soma}')
    