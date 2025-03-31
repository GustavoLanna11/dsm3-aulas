from tkinter import *

#criação da variavel
tela = Tk()
#titulo na barra de titulos
tela.title("Cadastro de Clientes")
#cor da tela
tela.configure(background='#1e3743')
#configurar tamanho da tela 
tela.geometry("700x600")

#define reajuste da tela
tela.resizable(True,True)
#tamanho maximo que a tela pode chegar
tela.maxsize(width=800, height=700)
#tamanho minimo que atela pode chegar
tela.minsize(width=500,height=300)


#colocando caixa de texto
lbl_titulo= Label(tela, text="CADASTRO DE CLIENTES", font="Arial 25 bold italic", bg='#1e3743',fg='#BCD1AD')
lbl_titulo.pack()

lbl_nome= Label(tela, text="Digite o nome: ", font="Arial 15 bold italic", bg='#1e3743',fg='#f0ffff')
lbl_nome.place(x=10, y=45)
txt_nome = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_nome.place(x=165, y=45)
txt_nome.insert(0,"Digite seu nome aqui")

lbl_email= Label(tela, text="Digite o e-mail: ", font="Arial 15 bold italic", bg='#1e3743',fg='#f0ffff')
lbl_email.place(x=10, y=85)
txt_email = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_email.place(x=165, y=85)
txt_email.insert(0,"Digite seu e-mail aqui")

lbl_telefone= Label(tela, text="Digite o telefone: ", font="Arial 15 bold italic", bg='#1e3743',fg='#f0ffff')
lbl_telefone.place(x=10, y=125)
txt_telefone = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_telefone.place(x=185, y=125)
txt_telefone.insert(0,"Digite seu telefone aqui")

lbl_endereco= Label(tela, text="Digite o endereço: ", font="Arial 15 bold italic", bg='#1e3743',fg='#f0ffff')
lbl_endereco.place(x=10, y=165)
txt_endereco = Entry(tela, width=60, borderwidth=5, fg="blue")
txt_endereco.place(x=205, y=165)
txt_endereco.insert(0,"Digite seu endereço aqui")


#definindo uma função
def mostrar_Dados():
    lbl_titulocliente = Label(tela, text="Dados do Cliente", font="Arial 20 bold italic", bg='#1e3743',fg='#BCD')
    lbl_titulocliente.place(x=205, y=200)
    lbl_ola = Label(tela, text="Nome:  " + txt_nome.get() + "\n Telefone:  " + txt_telefone.get() + "\n Endereço " + txt_endereco.get() + "\n E-mail: " + txt_email.get())
    lbl_ola.place(x=205, y=235)

    
#colocando botão 
btn_botao = Button(tela, text="Cadastrar Cliente", font="Arial 15 bold ", bg='#1ed', command=mostrar_Dados)
btn_botao.place(x=250, y=325)


def verificaFocusCaixa(event):    
    txt_nome.delete(0,END)

txt_nome.bind("<FocusIn>", verificaFocusCaixa)


#executa tela
tela.mainloop()