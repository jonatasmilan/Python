# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.


lista = [0, 1]
contador = 0 
while True:
    anterior = lista[contador]
    proximo = lista[contador + 1]
    resultado = anterior + proximo
    lista.append(resultado)
    contador += 1
    if lista [-1] >= 500:
        break

string = ', '.join(str(numero) for numero in lista)
print(string)