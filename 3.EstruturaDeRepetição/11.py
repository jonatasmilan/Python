# Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('insira um número: '))
n2 = int(input('insira um número: '))
soma = 0

if n1 > n2:
    for i in range(n2 + 1,n1):
        print(i)
        soma += i
    
elif n1 < n2:
    for i in range(n1 + 1,n2):
        print(i)
        soma += i
else:
    print('Os numeros são iguais.')

print(f'A soma é igual a {soma}')
        