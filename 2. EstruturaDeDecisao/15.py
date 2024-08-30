# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado_1 = float(input('Insira o valor de um lado: '))
lado_2 = float(input('Insira o valor de um lado: '))
lado_3 = float(input('Insira o valor de um lado: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print('Pode ser um triângulo')
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Triângulo equilátero')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('NÃO pode ser um triângulo')
    