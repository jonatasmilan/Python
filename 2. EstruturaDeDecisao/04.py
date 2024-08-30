# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Insira uma letra: ')
letra2 = letra.lower()

if letra2.isalpha() == True:
    if letra2 in 'aeiou':
        print('A letra é uma vogal.')
    else:
        print('A letra é uma consoante.')
else:
    print('Não é uma letra.')