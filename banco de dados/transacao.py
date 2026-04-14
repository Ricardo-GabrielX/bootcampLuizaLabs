import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# Transação é um conjunto de operações que devem ser executadas como uma unidade atômica, ou seja, ou todas as operações são executadas com sucesso ou nenhuma delas é executada.
# conexao.commit() é usado para confirmar as operações realizadas, ou seja, para salvar as alterações no banco de dados. Se ocorrer algum erro durante a execução das operações.
# podemos usar conexao.rollback() para desfazer as alterações realizadas até o ponto da última confirmação (commit). Isso garante a integridade dos dados e evita que o banco de dados fique em um estado inconsistente.
try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 3', 'joao@email.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (4, ?, ?)', ('Teste 4', 'joao@email.com'))
    conexao.commit()
except Exception as exc:
    print(f"Erro ao inserir cliente: {exc}")
    conexao.rollback()
