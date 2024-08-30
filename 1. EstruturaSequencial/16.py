# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

m2 = float(input('Área (m²) a ser pintada: '))
litros = m2 / 3
latas =litros / 18
print(f'{latas:.2f} latas e {latas * 80:.2f} reais')
