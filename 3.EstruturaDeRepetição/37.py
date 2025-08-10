'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados 
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

lista_codigo = []
lista_altura = []
lista_peso = []

while True:
    codigo = int(input('Qual seu código? '))
    if codigo == 0:
        break
    lista_codigo.append(codigo)
    altura = float(input('Qual sua altura? (cm) '))
    lista_altura.append(altura)
    peso = float(input('Qual seu peso? (kg) '))
    lista_peso.append(peso)

print(f'O mais alto é o de código {lista_codigo[lista_altura.index(max(lista_altura))]} de altura {max(lista_altura)} cm')
print(f'O mais baixo é o de código {lista_codigo[lista_altura.index(min(lista_altura))]} de altura {min(lista_altura)} cm')
print(f'O mais gordo é o de código {lista_codigo[lista_peso.index(max(lista_peso))]} de {max(lista_peso)} kg')
print(f'O mais magro é o de código {lista_codigo[lista_peso.index(min(lista_peso))]} de {min(lista_peso)} kg')
print(f'A média das alturas é {(sum(lista_altura) / len(lista_altura)):.2f} cm')
print(f'A média dps pesos é {(sum(lista_peso) / len(lista_peso)):.2f} kg')

    
    