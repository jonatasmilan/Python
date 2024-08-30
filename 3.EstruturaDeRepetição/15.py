# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input('insira um número para gerar a sequência: '))

lista = [1, 1]

if n == 0:
    print('0')
elif n == 1:
    print(lista[0])
elif n == 2:
    print(lista)
else:  
    for i in range(n - 2):
        anterior = lista[i]
        proximo = lista[i + 1]
        resultado = anterior + proximo
        lista.append(resultado)

string = ', '.join(str(numero) for numero in lista)
print(string)
