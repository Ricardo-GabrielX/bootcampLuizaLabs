import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(80), email VARCHAR(150))')


data = ('Giovanna Silva', 'joao.silva@example.com')
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
conexao.commit()