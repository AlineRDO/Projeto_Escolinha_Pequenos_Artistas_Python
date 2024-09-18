from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('escola.db')

# Rota para exibir o formulário de adicionar aluno
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar aluno
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    
    if nome and data_nascimento:
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Alunos (nome, data_nascimento) VALUES (?, ?)", (nome, data_nascimento))
        conexao.commit()
        conexao.close()
        
    return redirect(url_for('index'))

# Rota para exibir alunos
@app.route('/alunos')
def alunos():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    conexao.close()
    
    return render_template('alunos.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)
