'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''

divida = float(input('Valor da dívida: R$ '))
juros = [0, 0.1, 0.15, 0.20, 0.25]
parcelas = [1, 3, 6, 9, 12]
print(f'{'Valor da Dívida':20} {'Valor dos Juros':20} {'Qntde de Parcelas':20} {'Valor da Parcela':20}')

for i in range(len(parcelas)):
    divida_juros = divida * (juros[i] + 1)
    valor_juros = juros[i] * divida
    valor_parcela = divida_juros / parcelas[i]
    print(f'R$ {divida_juros:.2f} {valor_juros:20.2f} {parcelas[i]:20.2f} {valor_parcela:20.2f}')
    