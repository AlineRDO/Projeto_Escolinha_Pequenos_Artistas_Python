# Função para conectar e criar tabelas no banco de dados SQLite
def criar_banco_de_dados():
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    
    # Criação da tabela Alunos
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL
                    )''')
    
    # Criação da tabela Registros de Saúde
    cursor.execute('''CREATE TABLE IF NOT EXISTS RegistrosSaude (
                        id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_aluno INTEGER,
                        data_registro TEXT,
                        altura REAL,
                        peso REAL,
                        observacoes TEXT,
                        FOREIGN KEY(id_aluno) REFERENCES Alunos(id_aluno)
                    )''')
    
    conexao.commit()
    conexao.close()

# Chamando a função para criar o banco e as tabelas
criar_banco_de_dados()
