#Exemplo 5 - AD mais de uma label

from tkinter import *
tela = Tk()

tela.title("Fatec Registro")
tela.geometry("700x600")
tela.resizable(True, True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

lbl_nome = Label (tela, text="Nome".place(x=10, y=10))
lbl_cpf = Label (tela, text="CPF").place(x=10, y=50)
tela.mainloop()