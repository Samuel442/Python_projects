# Crie um script que receba números e imprima os números digitados e os números pares

# ---------------Variáveis e listas usadas
i = 0
numeros = []
quantidade_numeros = int(input("Digite a quantidade de némeros que você deseja verificar se é par incluindo o zero: "))
contador = 0


# ---------------Estrutura para repetir o número de vezes que o usuário digitar
while contador < quantidade_numeros:
    numeracao = input("Digite os numeros para verificar se é par incluindo o zero: ")
    numeros.append(numeracao)
    contador += 1
    if contador == quantidade_numeros:
        break


# -------------Estrutura para repetir o número de vezes para percorrer a lista
for i in range(len(numeros)):           # Tamanho da lista deleimita a repetição
    if i % 2 == 0:                      # Se o resto da divisão por 2 for 0
        print("Números pares: ", i)
print("Números digitados: ",numeros)