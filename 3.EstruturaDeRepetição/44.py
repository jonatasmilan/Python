'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

print('1 - Candidato 1\n'
'2 - Candidato 2\n'
'3 - Candidato 3\n'
'4 - Candidato 4\n'
'5 - Voto Nulo\n'
'6 - Voto em Branco')
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto_nulo = 0
voto_branco = 0

while True:
  voto = int(input('Qual o seu voto? '))
  if voto == 1:
    candidato_1 += 1
  if voto == 2:
    candidato_2 += 1
  if voto == 3:
    candidato_3 += 1
  if voto == 4:
    candidato_4 += 1
  if voto == 5:
    voto_nulo += 1
  if voto == 6:
    voto_branco += 1
  if voto == 0:
    break
total = candidato_1 + candidato_2 + candidato_3 + candidato_4 + voto_nulo + voto_branco
print(f'Candidato 1 teve {candidato_1} votos, o candidato 2 teve {candidato_2} votos, o candidato 3 teve {candidato_3} e o candidato 4 teve {candidato_4} votos;')
print(f'Tiveram {voto_nulo} votos nulos;')
print(f'Tiveram {voto_branco} votos em branco;')
print(f'A percentagem de votos nulos sobre o total de votos: {((voto_nulo) / (total)) * 100:.2f}')
print(f'A percentagem de votos em branco sobre o total de votos: {((voto_branco) / (total)) * 100:.2f}')