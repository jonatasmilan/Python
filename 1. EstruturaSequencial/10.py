# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# (c / 5) = (f - 32) / 9
c = float(input('Insira a temperatura em °C: '))
f = (c * (9 / 5)) + 32
print(f'A temperatura em Fahrenheit é {f:.2f}')
