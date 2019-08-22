senha = senha1 = senha01 = senha02 = 0
nome = ' '
usuario = ' '
criar = ' '
login = ' '
email = ' '
def projeto():
    from os import system as st
    st('cls')
    def cadastro():
        # while True:
        while True:
            try:
                global criar
                while True:
                    try:
                        criar = str(input('Deseja criar uma nova conta [S/N]: ')).strip().title()
                        if criar:
                            break
                    except:
                        criar = str(input('ERRO!!! Digite novamente, para continuar [S/N]: ')).strip().title()
                st('cls')
                if criar in 'Ss':
                    while True:
                        try:
                            global login
                            login = str(input('Digite um nome de usuário: '))
                            st('cls')
                            if login != usuario:
                                break
                        except:
                            print('ERRO!!! Usuário existente, tente outro')
                    global email
                    global senha01
                    global senha02
                    email = str(input('Digite o seu melhor email: '))
                    senha01 = int(input('Digite uma senha de números: '))
                    while True:
                        try:
                            senha02 = int(input('Repita a sua senha: '))
                            st('cls')
                            if senha02 == senha01:
                                break
                        except:
                            print('ERRO Digite uma senha igual a senha anterior')
                            st('cls')
                    if (((senha01 == senha02) != senha1) and (login != usuario)):
                        break
            except:
                print('ERRO!!!')
            else:
                print('Conta criada com sucesso!')
            # if criar in 'Nn':
            #     break
    def login (n, s):
        global nome
        global senha
        sistema_banco_de_dados(usuario, senha1)
        while True:
            try:
                nome = str(input('Nome: '))
                if nome:
                    break
            except:
                print('ERRO!!!')
        while True:
            try:
                # if senha.isdigit()
                senha = str(input('Senha: ')).strip().capitalize()
                st('cls')
                if senha:
                    break
            except:
                print('ERRO!!!')
        if nome == usuario and senha == senha1:
            print('Logado')
        else:
            print('Usuário ou senha inválido')
            cadastro()
    def sistema_banco_de_dados (u, s):
        global usuario
        global senha1
        usuario = 'estevam'
        senha1 =  'Respira'

    def continuar ():
        while True:
            login(usuario, senha1)
            resposta = ' '
            resposta = str(input('Deseja continuar [S/N]: ')).strip().title()
            st('cls')
            while resposta not in 'SsNn':
                resposta = str(input('ERRO!!! Digite novamente, para continuar [S/N]: ')).strip().title()
                st('cls')
            if resposta in 'Nn':
                break
    continuar()
projeto()
