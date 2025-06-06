# estrutura básica, edição de tela, botões

# Estrutura básica

# from tkinter import *
# import tkinter as tk

# tela = Tk()
# tela.mainloop()

# ------------------------------------------------ #

# Estrutura de tela, responsividade e label

# from tkinter import *
# import tkinter as tk
# tela = Tk()

# tela.title("Teste")
# tela.configure(background='#c0c0c0')
# tela.geometry("700x600")

# tela.resizable(True, True)
# tela.maxsize(width=800, height=700)
# tela.minsize(width=500, height=300)

# lbl_teste = Label(tela, text="TESTE").place(x=100, y=50)

# tela.mainloop()

# ------------------------------------------------ #

#label e configuração de label

# from tkinter import *
# tela = Tk()

# tela.title("Fatec Registro")
# tela.configure(background='#c9c9c9')
# tela.geometry("700x600")
# tela.resizable(True, True)
# tela.maxsize(width="1000", height="1000")
# tela.minsize(width="500", height="500")

# lbl_nome = Label(tela, text="Nome:", font="Arial 10", fg="#000000").place(x=200, y=50)
# lbl_cpf = Label(tela, text="CPF:", font="Arial 10", fg="#000000").place(x=200, y=100)

# tela.mainloop()

# ------------------------------------------------ #

# centralização da tela - NÃO FUNCIONOU!!!!!

# from tkinter import *
# # import tkinter as tk
# # tela = Tk()

# # tela.title("Teste do Gusta")
# # tela.configure(background='#c9c9c9')

# # largura = 800
# # altura = 300
# # largura_screen = tela.winfo_screenmmwidth()
# # altura_screen = tela.winfo_screenheight()
# # posx = largura_screen/2 - largura/2
# # posy = altura_screen/2 - altura/2

# # tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
# # tela.mainloop()

# ------------------------------------------------ #

# Criação de botão

# from tkinter import *
# import tkinter as tk
# tela = Tk()

# tela.configure(background='#c0c0c0')
# tela.geometry("700x700")
# tela.maxsize(width="1000", height="1000")
# tela.minsize(width="500", height="500")
# tela.title("Gustavo Lanna!")

# lbl_nome = Label(tela, text="Nome: ", font="Arial 10").place(x=350, y=250)
# lbl_cpf = Label(tela, text="CPF:", font= "Arial 10").place(x=350, y=300)

# btn_botao = Button(tela, text="Mim aperte 😈")
# btn_botao.pack()

# tela.mainloop()

# ------------------------------------------------ #

# configuração de botão

from tkinter import *
import tkinter as tk
tela = Tk()

tela.title("Gustavo Lanna")
tela.configure(background='#c0c0c0')
tela.geometry("1000x1000")
tela.resizable(True, True)
tela.maxsize(width="1050", height="1050")
tela.minsize(width="100", height="100")

lbl_teste = Label(tela, text="OPA, TESTE IRMAO", font="Arial 20").place(x=500, y=500)
btn_teste = Button(tela, text="BOTAO ME APERTE").place(x=500, y=600)

# função
txt_nome = Entry(tela, width=20, borderwidth=5)
txt_nome.pack()
txt_nome.insert(0,"Digite seu nome: ")

def meu_click():
    lbl_hello = Label(tela, text="Bem Vindo: " + txt_nome.get())
    lbl_hello.pack()

btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()

tela.mainloop()
