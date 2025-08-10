# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input('Insira um número inteiro: '))
div = 0

for i in range(2, n + 1):
    primo = True
    
    for c in range (2, i):
        div += 1
        if i % c == 0:
            primo = False
            break
    if primo:
        print(i)
        
print(f'O total de divisões foi: {div}')
