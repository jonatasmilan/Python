# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

a = int(input('insira o numero de habitantes: '))
b = int(input('insira o numero de habitantes: '))
anos = 0

if a < 0 or b < 0:
    print('valores inválidos.')
elif a > b:
    print('a população já é maior.')
else:
    while a < b:
        a += a * 0.03
        b += b * 0.015
        anos += 1

print(anos)