# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# 
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input('Insira a quantidade (kg) de morangos adquiridos: '))
macas = float(input('Insira a quantidade (kg) de maçãs adquiridos: '))
preco_total = 0

if morangos <= 5:
    preco_morango = 2.5 * morangos
else: 
    preco_morango = 2.2 * morangos

if macas <= 5:
    preco_maca = 1.8 * macas
else:
    preco_maca = 1.5 * macas
    
if (morangos + macas) > 8:
    preco_total = (preco_morango + preco_maca) - (preco_morango + preco_maca) * 0.1
else:
    preco_total = preco_maca + preco_morango
    
print(preco_total)