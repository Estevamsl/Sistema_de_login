senha = 0
nome = ' '
usuario = ' '
senha1 = ' '
def projeto():
    '''
        projetinho
                    '''
    from os import system as st
    st('cls')
    
    def login (n, s):
        global nome
        global senha
        sistema(usuario, senha1)
        while True:
            try:
                nome = str(input('Nome: '))
                if nome:
                    break
            except:
                print('ERRO!!!')
        while True:
            try:
                senha = int(input('Senha: '))
                if senha > 0:
                    break
            except:
                print('ERRO!!!')
        if nome == usuario and senha == senha1:
            print('Logado')
        else:
            print('Não logado')

    def sistema (u, s):
        global usuario
        global senha1
        usuario = 'tete'
        senha1 = 32377364

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