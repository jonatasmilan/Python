# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

salario = float(input('Digite o salário: '))
salario_final = 0
ajuste = ''
aumento = 0

if salario <= 280:
    salario_final = salario + salario * 0.2
    ajuste = '20%'
    aumento = 0.2 * salario
if salario > 280 and salario <= 700:
    salario_final = salario + salario * 0.15
    ajuste = '15%'
    aumento = 0.15 * salario
if salario > 700 and salario <= 1500:
    salario_final = salario + salario * 0.10
    ajuste = '10%'
    aumento = 0.1 * salario
if salario > 1500:
    salario_final = salario + salario * 0.05
    ajuste = '5%'
    aumento = 0.05 * salario

    
print(salario)
print(ajuste)
print(aumento)
print(salario_final)