from tkinter import *
import tkinter as tk
tela = Tk()

tela.title("Exercício 1")
tela.geometry("1000x1000")
tela.resizable (True, True)
tela.maxsize(width="1050", height="1050")
tela.minsize(width="600", height="600")
tela.configure(background='#c0c0c0')

lbl_num1 = Label (tela, text="Digite um número: ").place(x=500, y=200)
txt_num1 = Entry(tela, width=20, borderwidth=5)
txt_num1.pack()
txt_num1.insert(0, "")

lbl_num2 = Label (tela, text="Digite o segundo número: ").place(x=500, y=250)


tela.mainloop()