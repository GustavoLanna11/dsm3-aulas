#Exemplo 1 - Cor e tamanho

from tkinter import *
#criação da variável 
tela = Tk()

#Titulo na barra de tarefas
tela.title("Fatec Registro")

#configuração da cor da tela(opcional)
tela.configure(background= '#1e3743')

#configuração do tamanho da tela
tela.geometry("700x600")

tela.mainloop()