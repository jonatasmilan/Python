# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = (input("Data: "))

if int(data[0:2]) != 0  and int(data[0:2]) <= 31 :
    if int(data[3:5]) != 0  and int(data[3:5]) <= 12 :
        if int(data[6:11]) != 0 :
            print("Data Válida")
        else :
            print("Data Inválida")
    else :
        print("Data Inválida")
else:
    print("Data Inválida")