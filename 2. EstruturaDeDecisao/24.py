# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")


def checar():
    if (resultado // 1 == resultado):
        print("Inteiro")
    else: 
        print("Decimal")
    
    if resultado % 2 == 0:
        print("Par")
    else:
        print('Ímpar')
        
    if resultado > 0:
        print("Positivo")
    else:
        print("Negativo")



if operacao == '+':
    resultado = numero1 + numero2
    print("Resultado: ", resultado)
    checar()
elif operacao == '-':
    resultado = numero1 - numero2
    print("Resultado: ", resultado)
    checar()
elif operacao == '/':
    resultado = numero1 / numero2
    print("Resultado: ", resultado)
    checar()
elif operacao == '*':
    resultado = numero1 * numero2
    print("Resultado: ", resultado)
    checar()
else:
    print("Valor Invalido")