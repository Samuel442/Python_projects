# Criar um algoritmo que receba duas strings digitadas pelo usuário,
# imprimir o tamanho, dizer se elas são iguais ou não e dizer também
# quais itens são iguais nas duas strings


palavra_1 = str(input ("Digite a primeira palavra: "))
palavra_2 = str(input ("Digite a segunda palavra: "))

def igualdade_palavras():
    if palavra_1 == palavra_2:
        print("Palavras iguais!")
    print("\n")

def numero_letras():
    print("Número de letras da palavra 1: ", len(palavra_1))
    print("Número de letras da palavra 2: ", len(palavra_2))
    print('\n')

def imprime_item():
    for x in palavra_1:
        print(x)
    print("\n")
    for y in palavra_2:
        print(y)
    print('\n')

def verifica_item():                 # função que fala todos os itens que são repetidos
    palavra_3 = []                   # lista que armazena os itens repetidos
    for i in palavra_1:              # este laço percorre a primeira palavra porém para no primeiro item para o compilador ir no prox laço
        for j in palavra_2:          # com o laço anterior parado no item em análise, este laço percorre uma posição também
            if (i == j):             # uma vez percorrido duas posições, é feita uma verificação com if se os itens são iguais
                palavra_3.append(j)  # Caso seja iguais estes itens iguais vai para esta lista palavra_3
    print("Itens iguais em ambos: ",palavra_3) # Por fim é impresso apenas os itens iguais

igualdade_palavras()
numero_letras()
imprime_item()
verifica_item()