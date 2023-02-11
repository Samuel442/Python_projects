# Crie um script que armazene uma lista de nomes de pessoas que participarão do sorteio
# mas antes disso o scipt deve perguntar quantas pessoas participarão do sorteio
# posteriormente o script deve selecionar o vencedor do sorteio e também os participantes

import random

i = 0                   # variável de controle sempre começando vazia
j = 0                   # variável de controle sempre começando vazia
condicao = True         # condição é verdadeira
participantes = []      # lista de participantes vazia

while condicao == True:
    try:
        quantidade = int(input("Digite a quantidade de pessoas que prticiparão do sorteio: "))
    except:
        print("Digite apenas números!")
    else:
        condicao = False

while quantidade > 0:
    pessoas = str(input("Digite o nome dos participantes: "))
    participantes.append(pessoas)
    quantidade = quantidade - 1                                # Parada do while sempre diminui 1 no final do bloco

vencedor = random.choice(participantes)             # usando random pega na lista a pessoa aleatoria e armazena na variável vencedor
print("------------------------------------")
print("Vencedor do sorteio: ",vencedor)                                     # imprime o vencedor
print("------------------------------------")

for i in participantes:
    print("Participantes: ",i)
print("------------------------------------")