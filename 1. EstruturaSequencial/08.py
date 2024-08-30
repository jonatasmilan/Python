# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario = float(input('Quanto vc ganha por hora?\n'))
horas = float(input('Quantas horas trabalhadas no mês?\n'))
print(f'Seu salário nesse mês será de $ {(salario * horas):.2f}')
