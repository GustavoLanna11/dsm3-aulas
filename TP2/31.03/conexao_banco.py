#Exercício de conexão com o banco de dados
import sqlite3
import PIL from Image, ImageTK

tela = Tk()
tela.title("Controle de Pessoas")
var = StringVar()
var.set("m")
largura = 800
altura = 600

#cria database
conn = sqlite3.connect("MyDB.db")

#criar cursor
cur = conn.cursor()

#criar tabela
cur.execute("CREATE TABLE IF NOT EXISTS pessoas(codigo INT primary key, nome TEXT, idade INT, sexo TEXT, altura REAL, peso REAL, cidade TEXT, datanasc TEXT, dataAtual TEXT, dataCadastro TEXT, descricao TEXT)")
conn.commit()

#close connection
conn.close()

def insercao():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()

    #insere dados na tabela
    cur.execute('INSERT INTO pessoas VALUES (:codigo, :nome, :idade, :sexo, :altura, :peso, :cidade, :datanasc, :dataatual, :dataCadastro, :descricao)',
                {'codigo': txt_codigo.get(), 'nome': txt_nome.get(), 'idade':txt_idade.get(), 'sexo': var.get(), 'altura':txt_altura.get(), 'peso': txt_peso.get(), 'cidade': cmb_ciade.get(), 'dataasc':txt_data_nascimento.get(), 'dataatual':txt_data_atualizacao.get(), 'dataCadastro':txt_data_cadastro.get(), 'descricao':txt_descricao.get()})
    
    #commit changes
    conn.commit()

    #close connection
    conn.close()

    #Clear text boxes
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_altura.delete(0, END)
    txt_descricao.delete(0, END)

def consulta():
    conn = sqlite3.connect("MyDB.db")

    #Create cursor
    cur = conn.cursor()

    #faz consulta da tabela
    cur.execute('SELECT *, codigo FROM pessoas')

    records = cur.fetchall()

    #mostra resultados encontrados
    print_records = ""
    for rec in records:
        print_records += 'Codigo:' +str(rec[0])+'  Nome '+str(rec[1])+'\n Idade: '+str(rec[2])+' Sexo: '+str(rec[3]) + '\n Altura: '+str(rec[4]) + ' Peso: '+str(rec[5]) +' cidade: ' +str(rec[6]), +' dataasc: ' +str(rec[6]), +' dataatual: ' +str(rec[7]), +' dataCadastro: ' +str(rec[8]), +' descricao: ' +str(rec[9])

    # Create and positioning label for the result
    Label(tela, text=print_records).place(x = 20, y = 320)

    #Commit changes
    conn.commit()

    #close connection
    conn.close()

#Criando função delete 
def delete():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM pessoas WHERE codigo=' +txt_codigo.get())

    conn.commir()

    conn.close()
    messagebox.showinfo("Excluindo...", "Registro Excluído com sucesso")

def update():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    record_id = txt_codigo.get()

    cur.execute("""UPDATE pessoas set
        nome = :nome,
        idade = :idade,
        sexo = :sexo,
        altura = :altura,
        peso = :peso,
        cidade = :cidade,
        datanasc = :datanasc,
        dataCadastro = :dataCadastro,
        descricao = :descricao

        WHERE codigo = :codigo""",
        {
            'nome': txt_nome.get()
        }
    )
    