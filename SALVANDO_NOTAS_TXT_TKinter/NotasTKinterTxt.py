# janela em Tkinter que salva notas de alunos em txt

from tkinter import *

def salvando_dados():
    f = open("Dado.txt", "a")       # cria o arquivo txt e não sobrescreve os dados
    f.write("\nNome: ")
    f.write("%s\n" % nome.get())    # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("Nota de cálculo 1: ")
    f.write("%s\n" % nota_c1.get())  # pega o conteud da variavel nota_c1 e coloca na frente da string Nota de cálculo 1 no arquivo txt
    f.write("Nota de química: ")
    f.write("%s\n" % nota_quimica.get())  # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("Nota de desenho: ")
    f.write("%s\n" % nota_desenho.get())  # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("Nota de introdução a engenharia: ")
    f.write("%s\n" % nota_int.get())  # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("Nota de programação: ")
    f.write("%s\n" % nota_prog.get())  # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("Nota de geometria analítica: ")
    f.write("%s\n" % nota_ga.get())  # pega o cnteud da variavel nome e coloca na frente da string Nome no arquivo txt
    f.write("-----------------------------------------------")

    nome.delete(0,END)                      # limpa o campo nome
    nota_c1.delete(0, END)                  # limpa o campo nota calculo 1
    nota_quimica.delete(0, END)             # limpa o campo nota uimica
    nota_desenho.delete(0, END)             # limpa o campo nota desenho
    nota_int.delete(0,END)                  # limpa o campo nota de introdução a eng
    nota_prog.delete(0,END)                 # limpa o campo nota de programação
    nota_ga.delete(0,END)                   # limpa o campo nota de geometria
    f.close()

sistema = Tk()
sistema.title("1º período")
sistema.geometry("225x400")
sistema.configure(background = "#dde")


Label(sistema,text = "Nome do aluno:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 10,width = 100,height = 20) # cria um label nome
nome = Entry(sistema)                                                                                                             # entrada de dados
nome.place(x = 10,y = 30,width = 200,height = 20)

Label(sistema,text = "Nota de cálculo 1:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 60,width = 100,height = 20)
nota_c1 = Entry(sistema)                                                                                                             # entrada de dados única linha
nota_c1.place(x = 10,y = 80,width = 200,height = 20)

Label(sistema,text = "Nota de quimica:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 110,width = 100,height = 20)
nota_quimica = Entry(sistema)                                                                                                               # entrada de dados única linha
nota_quimica.place(x = 10,y = 130,width = 200,height = 20)

Label(sistema,text = "Nota de desenho:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 160,width = 100,height = 20)
nota_desenho = Entry(sistema)                                                                                                                 # entrada de dados única linha
nota_desenho.place(x = 10,y = 180,width = 200,height = 20)

Label(sistema,text = "Nota de introdução a engenharia:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 210,width = 185,height = 20)
nota_int = Entry(sistema)                                                                                                                 # entrada de dados única linha
nota_int.place(x = 10,y = 230,width = 200,height = 20)

Label(sistema,text = "Nota de programação:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 260,width = 125,height = 20)
nota_prog = Entry(sistema)                                                                                                                 # entrada de dados única linha
nota_prog.place(x = 10,y = 280,width = 200,height = 20)

Label(sistema,text = "Nota de geometria analítica:", background = "#808080",foreground = "#000", anchor = W).place(x = 10,y = 310,width = 185,height = 20)
nota_ga = Entry(sistema)                                                                                                                 # entrada de dados única linha
nota_ga.place(x = 10,y = 330,width = 200,height = 20)

Button(sistema,text = "Salvar",command = salvando_dados).place(x = 10,y = 360,width = 100,height = 20)

sistema.resizable(False,False)         # Não responsivo
sistema.mainloop()