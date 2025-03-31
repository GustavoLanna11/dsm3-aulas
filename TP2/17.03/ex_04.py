#Exemplo 4 - Adicionando Label

from tkinter import *
#criação da variável
tela = Tk()

#Título na barra de tarefas
tela.title("Fatec Registro")
#Configuração da cor da tela
tela.configure(background= '#1e3743')
#configuração do tamanho da tela
tela.geometry("700x600")

tela.resizable(True, True)
#Tamanho máximo que a tela pode chegar
tela.maxsize(width=800, height=700)
#tamanho mínimo que a tela pode chegar
tela.minsize(width=500, height=300)

lbl_teste = Label(tela, text="TESTE").place (x=10, y=10)
#lbl_teste é o nome de identificação interno da label
# Label é o grupo do componente
# tela é a variável que a label está ligado
# text="" é o texto a ser exibido na tela
#place o posicionamento da tela
tela.mainloop()