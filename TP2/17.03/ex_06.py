#Exemplo 6 - Interface no centro da tela
from tkinter import *
tela = Tk()
tela.title("Fatec Registro")

#dimensões da janela
largura=800
altura=300

#resolução do sistema(tela)
largura_screen = tela.winfo_screenmmwidth()
altura_screen = tela.winfo_screenheight()

#define o posicionamento centralizado
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#visualizaçãi do tamanho da tela no terminal
print(largura_screen, altura_screen)

#definição do geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()

#%d substitui um número, % concatena as variáveis referentes a cada %d
