#combobox
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Combobox")
janela.geometry('250x250')

combo = Combobox(janela)
combo['values']= ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati")
combo.current(1)
combo.pack()

janela.mainloop()

#CheckBox
# from tkinter import *
# tela = Tk()
# tela.title("open file")
# tela.geometry("300x600")

# def show():
#     Label(tela, text=var.get()).pack()

# var = StringVar()

# chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="off")
# chk_button.deselect()
# chk_button.pack()

# Button(tela, text="Show me", command=show).pack()

# tela.mainloop()


#Radiobutton
# from tkinter import *
# tela = Tk()

# tela.title("Radio Buttons")
# tela.configure(background='#1e3743')
# tela.geometry("700x600")

# var = StringVar()
# var.set("m")

# rdb_buttonm = Radiobutton(tela,text="M",variable=var, value="m").place(x=20, y=40)
# rdb_buttonf = Radiobutton(tela,text="F",variable=var, value="f").place(x=20, y=60)

# tela.mainloop()