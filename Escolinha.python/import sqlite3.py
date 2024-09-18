import sqlite3
from datetime import datetime

# Classe para representar um Aluno
class Aluno:
    def __init__(self, id_aluno, nome, data_nascimento):
        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return f"Aluno({self.id_aluno}, {self.nome}, {self.data_nascimento})"


# Classe para representar o Registro de Saúde
class RegistroSaude:
    def __init__(self, id_registro, id_aluno, data_registro, altura, peso, observacoes):
        self.id_registro = id_registro
        self.id_aluno = id_aluno
        self.data_registro = data_registro
        self.altura = altura
        self.peso = peso
        self.observacoes = observacoes

    def __repr__(self):
        return f"RegistroSaude({self.id_registro}, {self.id_aluno}, {self.data_registro}, {self.altura}, {self.peso}, {self.observacoes})"
