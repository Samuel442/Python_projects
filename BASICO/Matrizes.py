
# Estrutura da matriz 1
matriz_1 = [[0,0,0],
            [0,0,0],
            [0,0,0]]
#Estrutura da matriz 2
matriz_2 = [[0,0,0],
            [0,0,0],
            [0,0,0]]
#Estrutura da matriz de soma
soma = [[0,0,0],
        [0,0,0],
        [0,0,0]]

linha = 0          # variável para receber os valores das linhas
coluna = 0         # variável para receber os valores das colunas

def cria_matriz():
    # 2 for responsáveis por armazenar todos os elementos da matriz 1 percorrendo as linhas e colunas
    for linha in range(0,3):            # primeiro for responsável por percorrer cada linha
        for coluna in range(0,3):       # segundo for responsável por percorrer cada coluna
            matriz_1[linha][coluna] = float(input(f'Digite o elemento na pisição [{linha}] [{coluna}]: ')) # armazena os elementos
    print("----------------Matriz 2---------------------")
    # 2 for responsável por armazenar as linhas e colunas da matriz 2
    for linha in range(0,3):
        for coluna in range(0,3):
            matriz_2[linha][coluna] = float(input(f'Digite o elemento na posição: [{linha}] [{coluna}]: '))


def imprime_matriz():
    print("----------Matriz 1-----------")
    # 2 for responsáveis por imprimir a matriz com os elementos
    for linha in range(0,3):            # primeiro for responsável por percorrer cada linha
        for coluna in range(0,3):       # segundo for responsável por percorrer cada coluna
            print(f'[{matriz_1[linha][coluna]}]',end=' ') # imprime formatada a matrz de elementos
        print()                         # A cada linha ao final é quebrado
    # for responsável por exibir a matriz 2
    print("----------Matriz 2-----------")
    for linha in range(0,3):
        for coluna in range(0,3):
            print(f'[{matriz_2[linha][coluna]}]',end = ' ')
        print()


# Operação de soma de matrizes
def soma_matriz():
    for linha in range(0,3):
        for coluna in range(0,3):
            soma[linha][coluna] = matriz_1[linha][coluna] + matriz_2[linha][coluna]
            print(f'[{soma[linha][coluna]}]', end=' ')
        print()

print("Digite o elemento de cada matriz abaixo:")
print("-------------------------------------")
cria_matriz()
imprime_matriz()
print("-------Soma--------")
soma_matriz()
print("-------------------")