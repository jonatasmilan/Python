'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''
valor_total = 0
quantidade_cds = int(input('Qual a quantidade de CDs? '))
for i in range(1, quantidade_cds +1):
  valor = float(input(f'Insira o valor do CD {i}: '))
  valor_total += valor
  media = valor_total / quantidade_cds
print(f'O valor total investido foi R$ {valor_total:.2f} e o valor médio foi {media:.2f}')