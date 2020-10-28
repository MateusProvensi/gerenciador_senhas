import sqlite3
from usuario_interacao import interacao_usuario

conn = sqlite3.connect("senhas.db")

cursor = conn.cursor()

while True:
    opcao: str = interacao_usuario.menu()

    if opcao == '1':
        interacao_usuario.cadastrar_usuario(conn, cursor)
    elif opcao == '2':
        interacao_usuario.listar_usuarios_sem_senha(cursor)
    elif opcao == '3':
        interacao_usuario.apagar_usuario(conn, cursor)
    elif opcao == '4':
        interacao_usuario.alterar_senha(conn, cursor)
        pass
    elif opcao == '5':
        interacao_usuario.listar_usuarios_com_senhas(cursor)
        pass
    elif opcao == '6':
        exit()
    else:
        print('Opção não encontrada')

    print()
    print("-=" * 50)
