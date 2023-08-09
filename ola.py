'''
Programa exemplo de comandos básicos em python
'''
def ola(): #criando um comando sem parâmetro
    print('Olá feito em python!')
    print('Olá de novo')

def ola(nome): # criando um comando que recebe um valor
    print(f'Olá {nome}. Tudo bem?')

def tipos():
    nome = 'Maria'
    idade = 23
    salario = 2100.25
    print(f'Nome: {nome} \t\t-> Tipo: {type(nome)}')
    print(f'Idade: {idade} \t\t-> Tipo: {type(idade)}')
    print(f'Salário: {salario} \t-> Tipo: {type(salario)}')

# ola('João') este exemplo chama o comando ola sempre tendo Joao como nome
ola(input('Qual o seu nome? '))
