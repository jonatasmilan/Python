'''O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''


print(f'Especificação\t\tCódigo\t\tPreço\n',
'-' * 50,
'\nCachorro Quente\t\t100\t\tR$ 1,20',
'\nBauru Simples\t\t101\t\tR$ 1,30',
'\nBauru com ovo\t\t102\t\tR$ 1,50',
'\nHambúrguer\t\t103\t\tR$ 1,20',
'\nCheeseburguer\t\t104\t\tR$ 1,30',
'\nRefrigerante\t\t105\t\tR$ 1,00\n',
'-' * 50)
lista_codigos = [100, 101, 102, 103, 104, 105]
preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
while True:
  codigo = int(input('Qual o código do item? '))
  if codigo not in lista_codigos:
    print('Código inválido.')
    continue
  qntde = int(input('Qual a quantidade? '))
  check = input('Deseja parar? ')
  if check in 'Ss':
    break
