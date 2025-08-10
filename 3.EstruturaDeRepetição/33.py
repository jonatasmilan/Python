'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

lista = []
while True:
    temperatura = float(input('Temperatura: '))
    lista.append(temperatura)
    check = input('Deseja parar? ')
    if check in 'Ss':
        break


print(f'A menor temperatura é {min(lista)}')
print(f'A maior temperatura é {max(lista)}')
print(f'A média das temperatura é {sum(lista) / len(lista)}')
