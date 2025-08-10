'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

turmas = int(input('Qual o número de turmas? '))
total_alunos = 0

for i in range(1, turmas + 1):
    while True:
        alunos = int(input(f'Quantidade de alunos da turma {i} (máx. 40): '))
        if 1 <= alunos <= 40:
            total_alunos += alunos
            break
        else:
            print('Valor inválido! Digite um número entre 1 e 40.')

media = total_alunos / turmas
print(f'A média de alunos por turma é: {media:.2f}')