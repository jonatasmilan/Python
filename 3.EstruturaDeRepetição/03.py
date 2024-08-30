# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = str(input('insira o nome: '))
while len(nome) <= 3:
    print('valor inválido')
    nome = str(input('insira o nome: '))
    
idade = int(input('insira a idade: '))    
while idade < 0 or idade > 150:
    print('valor inválido')
    idade = int(input('insira a idade: '))
    
salario = float(input('insira o salário: '))   
while salario < 0:
    print('valor inválido')
    salario = float(input('insira o salário: '))
    
sexo = str(input('insira o sexo [f] ou [m]: '))   
while sexo !="f" and sexo!="m" :
    print('valor inválido')
    sexo = str(input('insira o sexo [f] ou [m]: '))
    
estado = str(input('insira o estado civil [s] [c] [v] [d]: '))    
while estado != "s" and estado != "c" and estado != "v" and estado != "d" :
    print('valor inválido')
    estado = str(input('insira o estado civil [s] [c] [v] [d]: '))

print('valores válidos!')                   