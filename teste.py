import sqlite3
from usuario_interacao import interacao_usuario

conn = sqlite3.connect("senhas.db")

cursor = conn.cursor()


senha = interacao_usuario.pegar_senha_master(cursor)
print(senha)
