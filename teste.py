senha = senha1 = senha01 = senha02 = acesso = 0
nome = ' '
usuario = ' '
criar = ' '
login = ' '
email = ' '
idade = 0
from random import choice
#-------#
# Class #
#-------#
class gerador():
    #---------#
    # FUNÇÕES #
    #---------#
    def gerador_senha(tamanho):
        caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
        senha = ""
        for i in range(tamanho):
            senha += choice(caracteres)
        return senha
    def pergunta_arquivo(resposta):
        
        while resposta != "sim" and resposta != "não" and resposta != "nao":
            resposta = input("Deseja salvar em um arquivo? sim/não: ")
        if resposta == "sim":
            nome_do_arquivo = input("Nome do arquivo: ")
            arquivo = open("{}.txt".format(nome_do_arquivo), "a") # Cria um atquivo no formato de escrita
            arquivo.write("NOME DE USUÁRIO: {}\n".format(nome)) # Escreve no arquivo
            arquivo.write("SENHA: {}\n".format(senha)) # Escreve no arquivo
            arquivo.write("LINK: {}".format(link)) # Escreve no arquivo
            arquivo.close() # Fecha o arquivo
            sair = input("Deseja sair? sim/não: ")
            while sair == "não" or sair == "nao":
                sair = input("Deseja sair? sim/não: ")
        elif resposta == "não" or resposta == "nao":
            print()
            print()
            print("+--------------------------")
            print("|Nome de Usuário: {}".format(nome))
            print("|Senha: {}".format(senha))
            print("|Link: {}".format(link))
            print("+--------------------------")
            print()
            sair = input("Deseja sair? sim/não: ")
            while sair == "não" or sair == "nao":
                sair = input("Deseja sair? sim/não: ")
    def pergunta_link(resposta):
        link = ""
        while resposta != "sim" and resposta != "não" and resposta != "nao":
            resposta = input("Quer digitar o link do site? sim/não: ")
        if resposta == "sim":
            link = input("Digite o link do site: ") 
        return resposta, link # retorna o valor de duas variaveis

def projeto():
    '''
        projetinho, está dando certo
                    '''
    from os import system as st
    from time import sleep as sp
    st('cls')

    def qtd_acesso():
        global acesso
        acesso += 1
    #     print(f'Foi {acesso} acessos')

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
                        qtd_acesso()
                        try:
                            global login
                            login = str(input('Digite um nome de usuário: ')).lower()
                            st('cls')
                            if login != usuario:
                                break
                        except:
                            print('ERRO!!! Usunetflix://rio existente, tente outro')
                    global email
                    global senha01
                    global senha02
                    while True:
                        try:
                            global idade
                            idade = int(input('Digite a sua idade: '))
                            st('cls')
                            # if not idade.isnumeric() or idade.isspace():
                            if idade > 17:
                                break
                                # idade = int(idade)
                        except:
                            print('Favor usar uma idade maior ou igual a 18 anos')
                        else:
                            print('Perfeito, idade ideal')
                    email = str(input('Digite o seu melhor email: '))
                    print('''[1] criar uma senha: 
[2] gerar senha: ''')
                    opcao = int(input('Escolha sua opção: '))
                    st('cls')
                    if opcao == 1:
                        senha01 = int(input('Digite uma senha de números: '))
                        while True:
                            try:
                                senha02 = int(input('Repita a sua senha: '))
                                sp(1)
                                # st('cls')
                                if senha02 == senha01:
                                    break
                            except:
                                print('ERRO, Digite uma senha igual a senha anterior')
                                st('cls')
                        if (((senha01 == senha02) != senha1) and (login != usuario)):
                            break
                        # print('Conta criada com sucesso!')
                    elif opcao == 2:
                        #--------------------#
                        # CORPO DO DOCUMENTO #
                        #--------------------#
                        print()
                        print("-------------------------")
                        print("GERADOR DE SENHAS PASSRAP")
                        print("-------------------------")
                        print("Info: Este programa irá gerar uma senha para ser utilizada em cadastros e contas!")
                        print()
                        # nome1 = input("Digite o nome de usuário: ")
                        quantidade = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))
                        pergunta_link = input("Quer digitar o link do site? sim/não: ")
                        pergunta_link, link = gerador.pergunta_link(pergunta_link) # usa duas variaveis para salvar os dois valores retornados pelo return da função
                        #-------------------#
                        # GERADOR DE SENHAS #
                        #-------------------#
                        senha03 = gerador.gerador_senha(quantidade)
                        print("SUA SENHA É: {}".format(senha))
                        print()
                        pergunta = input("Deseja salvar em um arquivo? sim/não: ")
                        pergunta = gerador.pergunta_arquivo(pergunta)
            except:
                print('ERRO!!!')
            # else:
            #     print('Conta criada com sucesso!')
            print('Conta criada com sucesso!')
            if criar in 'Nn':
                break
            
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
    print(f'Foi {qtd_acesso} contas criadas')
projeto()