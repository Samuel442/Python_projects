# Lista de compras, faça que o usuário digite o número de produtos para comprar,
# em seguida armazene um a um cada item, guardando em uma lista,
# posteriormente imprima os elementos da lista

repetir = True
compras = []    # Cria lista vazia

while repetir == True:
    try:                                                                             # Verifica se foi realmente digitado um número
        quantidade = int(input("Digite o número de itens que você vai comprar: "))   # armazena o número de itens que será adquirido
    except:                                                                          # Caso não seja um número
        print("Digite apenas números!")                                              # Alerta o usuário a digitar somente números
    else:
        repetir = False                                                              # Condição de parada do while

while quantidade > 0:                              # Caso o usuário não digite 0 produtos entra na repetição
    produtos = input("Digite o produto: ")         # Armanzena os produtos um a um na variável produtos
    compras.append(produtos)                       # Adiciona produtos no final da lista de compras
    quantidade = quantidade - 1                    # Decrementa a quantidade sempre de um em um até zerar a quantidade e sair do loop

print("----------Lista de compras------------")
for i in compras:                                  # com a variável i iniciando vazia ela percorre a lista de compras item a item
    print(i)                                       # imprime cada item



