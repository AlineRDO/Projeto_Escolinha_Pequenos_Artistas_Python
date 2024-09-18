import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para adicionar aluno ao banco de dados
def adicionar_aluno():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    
    if nome and data_nascimento:
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Alunos (nome, data_nascimento) VALUES (?, ?)", (nome, data_nascimento))
        conexao.commit()
        conexao.close()
        
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_data_nascimento.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Função para exibir os alunos cadastrados
def exibir_alunos():
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    conexao.close()
    
    listbox_alunos.delete(0, tk.END)
    for aluno in alunos:
        listbox_alunos.insert(tk.END, f"{aluno[0]} - {aluno[1]} ({aluno[2]})")

# Interface Tkinter
root = tk.Tk()
root.title("Sistema de Alunos")

# Labels e Entradas
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_data_nascimento = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):")
label_data_nascimento.pack()
entry_data_nascimento = tk.Entry(root)
entry_data_nascimento.pack()

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.pack()

btn_exibir = tk.Button(root, text="Exibir Alunos", command=exibir_alunos)
btn_exibir.pack()

# Listbox para exibir alunos
listbox_alunos = tk.Listbox(root)
listbox_alunos.pack()

root.mainloop()
