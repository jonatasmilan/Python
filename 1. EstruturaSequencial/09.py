# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
fahrenheit = float(input('Insira a temperatura em Fahrenheit: '))
celsius = 5 * ((fahrenheit-32) / 9)
print(f'A temperatura em Celsius é: {celsius:.2f}')
