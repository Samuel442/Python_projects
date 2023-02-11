# le o nome do aluno e nota, em seguida informa se está aprovado ou reprovado assim como a média

opcao = str(input("Desja cadastrar aluno? Digite: 'sim' para cadastrar ou 'não' para sair!      "))

while opcao == 'sim':
    aluno = str(input("Digite o nome do aluno: "))
    nota_calculo = float(input("Digite a nota de cálculo: "))
    nota_desenho = float(input("Digite a nota de desenho: "))
    nota_quimica = float(input("Digite a nota de quimica: "))
    nota_programacao = float(input("Digite a nota de programação: "))
    nota_eng = float(input("Digite a nota de introdução a engenharia: "))

    media = (nota_calculo + nota_desenho + nota_quimica + nota_programacao + nota_eng) / 5

    if media >= 60:
        print("Boa média!")
    else:
        print("Abaixo!")

    print("Aluno: ",aluno)
    print("Media: ",media)
    exit()

