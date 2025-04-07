# pip install pymongo

from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo

tela = Tk()
tela.title("Exemplo Mongo DB")
tela.geometry("800x600")
tela.resizable(True, True)
tela.configure(background="#fffff")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry (tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "")

lbl_cpf = Label(tela, text="CPF:", bg="#ffffff").place(x=450, y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cpf.place(x=480, y=170)
txt_cpf.insert(0, "")

lbl_idade = Label(tela, text="Idade:", bg="#ffffff").place(x=130, y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=190, y=200)
txt_idade.insert(0, "")

lbl_end = Label(tela, text="Rua:", bg="#ffffff").place(x=450, y=500)
txt_end = Entry (tela, width=25, borderwidth=2, fg="black", bg="white")
txt_end.place(x=480, y=200)
txt_end.insert(0, "")

lbl_bairro = Label(tela, text="Bairro:", bg="#ffffff").place(x=450, y=500)
txt_bairro = Entry (tela, width=25, borderwidth=2, fg="black", bg="white")
txt_bairro.place(x=190, y=230)
txt_bairro.insert(0, "")
