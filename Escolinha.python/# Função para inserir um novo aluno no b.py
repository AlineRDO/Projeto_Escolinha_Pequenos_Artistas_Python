# Função para inserir um novo aluno no banco de dados
def inserir_aluno(nome, data_nascimento):
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO Alunos (nome, data_nascimento) VALUES (?, ?)", (nome, data_nascimento))
    
    conexao.commit()
    conexao.close()

# Função para inserir um novo registro de saúde para um aluno
def inserir_registro_saude(id_aluno, altura, peso, observacoes):
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    
    data_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''INSERT INTO RegistrosSaude (id_aluno, data_registro, altura, peso, observacoes)
                      VALUES (?, ?, ?, ?, ?)''', (id_aluno, data_registro, altura, peso, observacoes))
    
    conexao.commit()
    conexao.close()

# Função para consultar todos os alunos
def consultar_alunos():
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    
    conexao.close()
    return alunos

# Função para consultar todos os registros de saúde de um aluno
def consultar_registros_saude(id_aluno):
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM RegistrosSaude WHERE id_aluno = ?", (id_aluno,))
    registros = cursor.fetchall()
    
    conexao.close()
    return registros
