import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# Jeito errado, um usuário malicioso pode colocar uma consulta ou uma manipulação de dados no nosso banco.
# Ou pode apagar alguma coisa, talvez um registro, ou a própria tabela. 
# id_cliente = input("Informe o id do cliente: ")
# cliente = cursor.execute(f'SELECT * FROM clientes WHERE ID = {id_cliente}')
# cliente = cursor.fetchone()
# print(dict(cliente))


id_cliente = input("Informe o id do cliente: ")
cliente = cursor.execute(f'SELECT * FROM clientes WHERE ID = {id_cliente}')

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))

