'''Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

n = int(input('Insira um número inteiro: '))
lista_primos = []

for i in range(2, n + 1):
    primo = True
    
    for c in range (2, i):
        if i % c == 0:
            primo = False
            break
    if primo:
        lista_primos.append(i)
print(lista_primos)
        

