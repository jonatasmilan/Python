'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_hora = float(input('Valor da hora: '))
horas = float(input('Horas trabalhadas: '))
salario_bruto = valor_hora * horas
imposto_renda = 0
sindicato = 0.03 * salario_bruto
fgts = 0.11 * salario_bruto
inss = 0.1 * salario_bruto

if salario_bruto <= 900:
    imposto_renda = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    imposto_renda = 0.05 * salario_bruto
elif salario_bruto > 1500 and salario_bruto <= 2500:
    imposto_renda = 0.1 * salario_bruto
else: 
    imposto_renda = 0.2 * salario_bruto
    


print(f'''
      Salário Bruto:                    : R$ {salario_bruto}
        (-) IR                          : R$ {imposto_renda}   
        (-) INSS ( 10%)                 : R$ {inss}
        FGTS (11%)                      : R$ {fgts} 
        Total de descontos              : R$ {imposto_renda + inss + sindicato}
        Salário Liquido                 : R$ {salario_bruto - (imposto_renda + inss + sindicato)} 
      ''')