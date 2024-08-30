# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#   Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

m2 = float(input('Área (m²) a ser pintada: '))
litros = m2 / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

#1
print(f'Serão necessárias {latas} latas e {latas * 80} reais')

#2
print(f'Serão utilizados {galoes} galões e {galoes * 25} reais')

#3
