# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
# conforme o caso.

turno = input('Em que turno você estuda? [M]atutino [V]espertino [N]oturno: ')
turno2 = turno.lower()

if turno2 == 'm' or turno2 == 'matutino':
    print('Bom dia!')
elif turno2 == 'v' or turno2 == 'vespertino':
    print('Boa tarde!')
elif turno2 == 'n' or turno2 == 'noturno':
    print('Boa noite!')
else:
    print('Valor inválido!')