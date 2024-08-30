# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Qual seu sexo? [M]asculino [F]eminino\n')
sexoMinusculo = sexo.lower()

if sexoMinusculo == 'masculino' or sexoMinusculo == 'm':
    print('M - Masculino')
elif sexoMinusculo == 'feminino' or sexoMinusculo == 'f':
    print('F - Feminino')
else:
    print('Sexo Inválido')