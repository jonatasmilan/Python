# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

respostas = 0

pergunta1 = input('Telefonou para a vítima? ')
if pergunta1 == 's':
    respostas += 1
pergunta2 = input('Esteve no local do crime? ')
if pergunta2 == 's':
    respostas += 1
pergunta3 = input('Mora perto da vítima? ')
if pergunta3 == 's':
    respostas += 1
pergunta4 = input('Devia para a vítima? ')
if pergunta4 == 's':
    respostas += 1
pergunta5 = input('Já trabalhou com a vítima? ')
if pergunta5 == 's':
    respostas += 1
    
if respostas == 2:
    print('Suspeita')
elif respostas >= 3 and respostas <= 4:
    print('Cúmplice')
elif respostas == 5:
    print('Assassino')
else:
    print('Inocente')
