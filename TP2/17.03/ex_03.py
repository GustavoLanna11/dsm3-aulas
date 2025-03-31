#Exemplo 3 - Reajuste de tela

from tkinter import *
#criação da variável
tela = Tk()

#titulo na barra de tarefas
tela.title("Fatec Registro")
#configuração da cor da tela (opcional)
tela.configure(background= '#1e3743')
#configuração do tamanho da tela
tela.geometry("700x600")

tela.resizable(True, True)
#máximo que a tela pode chegar
tela.maxsize(width=800, height=700)

#tamanho mínimo que a tela pode chegar
tela.minsize(width=500, height=300)
tela.mainloop()