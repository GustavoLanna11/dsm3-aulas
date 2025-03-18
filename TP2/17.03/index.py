# # from tkinter import *
# tela = Tk()

# tela.title("Fatec de Registro")
# tela.configure(background='#133333')
# tela.geometry("480x320")
# tela.resizable(True, True)
# tela.maxsize(width=760, height=400)
# tela.minsize(width=300, height=200)

# lbl_nome = Label(tela, text="Nome: ", bg=tela.cget("bg"), fg="white", font="Arial").place (x=10, y=10)
# lbl_telefone = Label(tela, text="Telefone: ", bg=tela.cget("bg"), fg="white", font="Arial").place (x=10, y=40)
# lbl_endereco = Label(tela, text="Endereço: ", bg=tela.cget("bg"), fg="white", font="Arial").place (x=10, y=70)
# lbl_cpf = Label(tela, text="CPF: ", bg=tela.cget("bg"), fg="white", font="Arial").place (x=10, y=100)

# btn_botao = Button(tela, text="Clicar")
# btn_botao.pack()


# tela.mainloop()


from tkinter import *
tela = Tk()
txt_nome = Entry(tela, width=50, fg="black", bg="#133753", borderwidth=5)
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome: ")

def clicar():
    lbl_nome = Label (tela, text="Bem vindo" + txt_nome.get())
    lbl_nome.pack()

btn_botao = Button(tela, text="Clique", command=clicar)
btn_botao.pack()
tela.mainloop()