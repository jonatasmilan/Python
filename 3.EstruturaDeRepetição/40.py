'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

Código da cidade;

Número de veículos de passeio (em 1999);

Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

Qual o maior e menor índice de acidentes de transito e a que cidade pertence;

Qual a média de veículos nas cinco cidades juntas;

Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

codigo = []
veiculos = []
acidentes = []
media_2000 = []

for i in range(1, 6):
  codigo.append(int(input('Código da cidade: ')))
  veiculos.append(int(input('Número de veículos de passeio: ')))
  acidentes.append(int(input('Número de acidentes de trânsito com vítimas: ')))
for c in range(len(veiculos)):
    if veiculos[c] < 2000:
        media_2000.append(acidentes[c])

print(f'O maior índice de acidentes de trânsito é {max(acidentes)} pertencente a cidade de código {codigo[acidentes.index(max(acidentes))]}')
print(f'O menor índice de acidentes de trânsito é {min(acidentes)} pertencente a cidade de código {codigo[acidentes.index(min(acidentes))]}')
print(f'A média de veículos nas cinco cidades juntas é de {sum(veiculos) / len(veiculos):.2f}')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de {sum(media_2000) / len(media_2000):.2f}')