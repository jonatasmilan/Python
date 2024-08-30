# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   
# Álcool:
#    até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro
# Gasolina:
#    até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 
# 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
#   (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
#   sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input('Quantos litros: '))
tipo = input('Tipo de combustível (G ou A): ')
preco_gasolina = litros * 2.5
preco_alcool = litros * 1.9

if tipo == 'A':
    if litros < 20:
        preco_alcool = preco_alcool - (0.03 * litros)
        print('O preço a ser pago é:', preco_alcool)
    else:
        preco_alcool = preco_alcool - (0.05 * litros)
        print('O preço a ser pago é:', preco_alcool)
elif tipo == 'G':
    if litros < 20:
        preco_gasolina = preco_gasolina - (0.04 * litros)
        print('O preço a ser pago é:', preco_gasolina)
    else:
        preco_gasolina = preco_gasolina - (0.06 * litros)
        print('O preço a ser pago é:', preco_gasolina)
else:
    print('Valores inválidos.')