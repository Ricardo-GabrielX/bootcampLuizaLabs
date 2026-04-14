import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)
cursor = conexao.cursor()


def criar_tabela(cursor, conexao):
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(80), email VARCHAR(150))')
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id=? ;', data)
    conexao.commit()

atualizar_registro(conexao, cursor, 1, 'Maria', 'maria@example.com')
atualizar_registro(conexao, cursor, 2, 'Maria', 'giovanaAtualizada@example.com')