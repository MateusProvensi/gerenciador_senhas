def pegar_senha_master(cursor) -> str:
    senha_tupla = cursor.execute(
        '''
        SELECT * FROM senha_master
        '''
    )
    senha_master = None
    for id_senha, senha in senha_tupla:
        senha_master = senha
    return senha_master


def menu() -> str:
    print()
    print(f'{"MENU PRINCIPAL":*^25}')
    print(
        '1 - Cadastrar um usuario\n'
        '2 - Listar usuarios\n'
        '3 - Apagar um usuario\n'
        '4 - Alterar uma senha\n'
        '5 - Visualizar senhas\n'
        '6 - Sair'
    )
    print()
    escolha: str = input("Digite sua escolha: ")
    print("-=" * 50)
    print()
    return escolha


def cadastrar_usuario(conn, cursor) -> None:

    servico: str = input('Digite o nome do servico: ')
    username: str = input('Digite o username do seu servico: ')
    senha: str = input('Digite a senha do seu servico: ')

    cursor.execute(
        f'''
        INSERT INTO usuario (servico, username, senha)
        VALUES
        ('{servico}', '{username}', '{senha}')
        '''
    )
    conn.commit()


def listar_usuarios_sem_senha(cursor) -> None:
    usuarios_tupla = cursor.execute(
        '''
        SELECT id_usuario, servico, username 
        FROM usuario
        '''
    )
    print(f'{"ID":<3} | {"SERVICO":<20} | {"USERNAME":<30}')
    print('-' * 59)
    for id_usuario, servico, username in usuarios_tupla:
        print(f'{id_usuario:<3} - {servico:<20} = {username:<30}')
        print('-' * 59)


def apagar_usuario(conn, cursor) -> None:
    listar_usuarios_sem_senha(cursor)
    print()
    senha_verificar = input('Digite a senha master para excluir um usuario: ')
    if not senha_verificar == pegar_senha_master(cursor):
        print('Senhas incorreta')
        return
    print()

    id_excluir = int(input('Digite o id para excluir: '))

    cursor.execute(
        f'''
        DELETE 
        FROM usuario 
        WHERE id_usuario = {id_excluir}
        '''
    )

    conn.commit()


def alterar_senha(conn, cursor) -> None:
    listar_usuarios_sem_senha(cursor)
    print()
    senha_verificar = input('Digite a senha master para excluir um usuario: ')
    if not senha_verificar == pegar_senha_master(cursor):
        print('Senhas incorreta')
        return
    print()

    id_alterar = int(input("Digite o id para alterar a senha: "))
    senha_nova = input("Digite a nova senha: ")

    cursor.execute(
        f'''
        UPDATE usuario 
        SET senha = '{senha_nova}'
        WHERE id_usuario = {id_alterar}
        '''
    )
    conn.commit()


def listar_usuarios_com_senhas(cursor) -> None:
    senha_verificar = input('Digite a senha master para excluir um usuario: ')
    if not senha_verificar == pegar_senha_master(cursor):
        print('Senhas incorreta')
        return
    print()

    usuarios_tupla = cursor.execute(
        '''
        SELECT * FROM usuario
        '''
    )

    print(f'{"ID":<3} | {"SERVICO":<20} | {"USERNAME":<30} | {"SENHA":<20}')
    print('-' * 82)
    for id_usuario, servico, username, senha in usuarios_tupla:
        print(f'{id_usuario:<3} - {servico:<20} = {username:<30} = {senha:<20}')
        print('-' * 82)
