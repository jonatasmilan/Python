# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Insira o raio (cm) do círculo:\n'))
area = math.pi * (raio ** 2)
print(f'A área do círculo é: {area:.2f} cm²')
