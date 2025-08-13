'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
que o usuário digite o salário inicial do funcionário.'''

from datetime import datetime

salario_inicial = float(input('Qual o seu salário inicial? '))
ano_inicial = 1995
ano_atual = datetime.now().year

percentual = 0.015
salario = salario_inicial

for i in range(ano_inicial + 1, ano_atual + 1):
  salario += salario * percentual
  if i > 1997:
    percentual *= 2

print(f'Salário em {ano_atual}: R$ {salario}')