import ntpath
from tkinter import *
import os

caminho = os.path.dirname(__file__)         # gera o caminho
nome_arquivo = caminho+"\\Contatos.txt"     # acossia a variável o caminho

def salva_data():
    arquivo = open(nome_arquivo,"a")                                # função para abertura do arquivo e anexa os dados
    arquivo.write("Nome.................:%s" %nome.get())           # grava no arquivo de texto o nome
    arquivo.write("\nSobrenome............:%s" % sobrenome.get())   # grava no arquivo o sobrenome da pessoa
    arquivo.write("\nTelefone.............:%s" % telefone.get())    # grava no arquivo o telefone da pessoa
    arquivo.write("\n\n\n")                                         # pula 3 linhas
    arquivo.close()                                                 # fecha o arquivo

interface = Tk()
interface.title("Agenda de contatos")                  # título da janela
interface.geometry("500x300")                          # tamanho da janela
interface.configure(background = "#6495ED")            # cor de fundo



Label(interface,text = "Nome", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 10,width = 100,height = 20) # cria um label nome
nome = Entry(interface)                                                                                                             # entrada de dados
nome.place(x = 10,y = 30,width = 200,height = 20)                                                                                   # posiciona


Label(interface,text = "Sobrenome", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 60,width = 100,height = 20)
sobrenome = Entry(interface)                                                                                                             # entrada de dados única linha
sobrenome.place(x = 10,y = 80,width = 200,height = 20)                                                                                   # posiciona


Label(interface,text = "Telefone", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 110,width = 100,height = 20)
telefone = Entry(interface)                                                                                                               # entrada de dados única linha
telefone.place(x = 10,y = 130,width = 200,height = 20)                                                                                    # posiciona


Label(interface,text = "E-mail", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 160,width = 100,height = 20)
email = Entry(interface)                                                                                                                 # entrada de dados única linha
email.place(x = 10,y = 180,width = 200,height = 20)                                                                                      # posiciona

Button(interface,text = "Salvar",command = salva_data).place(x = 10,y = 210,width = 100,height = 20)                                    # cria um botão de salvar
interface.mainloop()                                                                                                                    # loop do programa