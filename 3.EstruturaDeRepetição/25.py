#  Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se 
# a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

numero_pessoas = 0
soma_idades = 0
while True:
    idade = int(input('Insira uma idade: '))
    numero_pessoas += 1
    soma_idades += idade
    media = soma_idades / numero_pessoas
    check = input('Deseja parar? ')
    if check in 'Ss':
        break
if 0 < media <= 25:
    print(f'A média das idades é {media:.2f}. A turma é jovem (0 a 25 anos).')
if 25 < media <= 60:
    print(f'A média das idades é {media:.2f}. A turma é adulta (26 a 60 anos).')
if media > 60:
    print(f'A média das idades é {media:.2f}. A turma é idosa (maior que 60 anos).')