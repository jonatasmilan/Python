# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
base = int(input("base: "))
expoente = int(input("expoente: "))

potencia = 1

for i in range(expoente):
    potencia *= base
    i += 1

print(base,"^",expoente,"=",potencia)