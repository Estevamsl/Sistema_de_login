from random import choice
from os import system as st
from time import sleep as sp


#-----------------------#
# LOCAL VARIÁVEL GLOBAL #
#-----------------------#
senha = senha1 = senha01 = senha02 = acesso = conta_criada = idade = contador = 0
nome = ' '
usuario = ' '
criar = ' '
login = ' '
email = ' '
link = ''
cpf = ''
email01 = ''


#------------#
# FUNÇÃO CPF #
#------------#
def CPF(cpf):
    # while True:
    # global novo_cpf
    # cpf = str(input('Digite o seu cpf'))
    novo_cpf = cpf[:-2]
    total = 0
    reverso = 10
    
    for c in range(19):
        if c > 8:
            c -= 9
        total += int(novo_cpf[c]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    while True:
        try:
            if cpf == novo_cpf:
                print(f'CPF {cpf} \033[34mválido\033[m')
                break
        except:
            print(f'CPF {cpf} inválido')
            continue
        # return CPF() 
        
        
#-------------------------#
# FUNÇÃO CONVERTER NÚMERO #
#-------------------------#        
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except (ValueError, TypeError):
        try:
            valor = float(valor)
            return valor
        except (ValueError, TypeError):
            pass
            try:
                valor = str(valor)
                return valor
            except (ValueError, TypeError):
                pass
                try:
                    valor = bool(valor)
                    return valor
                except (ValueError, TypeError):
                    pass


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
        global link
        while resposta != "Ss" and resposta != "nN" and resposta != "não":
            resposta = input("Deseja salvar em um arquivo? sim/não: ")
        if resposta == "s":
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
            while sair == "não" or sair == "nao" or sair == 'n' or sair == 'N' or sair == 'Nao' or sair == 'NAO' or sair == 'NÃO':
                sair = input("Deseja sair? sim/não: ")


    def pergunta_link(resposta):
        global link
        link = ""
        while resposta != "sim" and resposta != "não" and resposta != "nao":
            resposta = input("Quer digitar o link do site? sim/não: ")
        if resposta == "sim":
            link = input("Digite o link do site: ") 
        return resposta, link # retorna o valor de duas variaveis


#------------------#
# FUNÇÃO PRINCIPAL #
#------------------#
def projeto():
    '''
        projetinho, está dando certo
                    '''
    st('cls')


    #-----------------#
    # FUNÇÃO CADASTRO #
    #-----------------#
    def cadastro(): # função para cadastrar o usuário
        # while True:
        while True:
            try:
                global criar
                while True:
                    try:
                        criar = str(input('Deseja criar uma nova conta [S/N]: \033[33m')).strip().title()
                        print('\033[m', end='')
                        if criar:
                            break
                    except:
                        criar = str(input('\033[31mERRO!!! Digite novamente, para continuar [S/N]:\033[m \033[31m')).strip().title()
                        print('\033[m', end='')
                st('cls')
                if criar in 'Ss':
                    while True:
                        global conta_criada
                        try:
                            global login
                            print('Digite um nome de usuário diferente do já criado e maior que 6 caracteres')
                            login = str(input('Digite um nome de usuário: \033[33m')).lower()
                            print('\033[m', end='')
                            st('cls')
                            if login != usuario and (len(login) > 6):
                                break
                        except:
                            print('ERRO!!! Usunetflix://rio existente, tente outro')
                    global email
                    global senha01
                    global senha02
                    cpf = str(input('Digite o seu cpf: \033[35m'))
                    print('\033[m', end='')
                    CPF(cpf)
                        
                    sp(0.7)
                    st('cls')
                    while True:
                        try:
                            global idade
                            idade = int(input('Digite a sua idade: \033[33m'))
                            print('\033[m', end='')
                            st('cls')
                            # if not idade.isnumeric() or idade.isspace():
                            if idade > 17:
                                break
                            # elif type(idade) != str or type(idade) != float:
                            #     break
                                # idade = int(idade)
                        except:
                            print('Favor usar uma idade maior ou igual a 18 anos ou idade diferente de str ou float')
                        # except (TypeError, ValueError):
                        #     print('Digite uma idade inteira')
                        else:
                            print('\033[31mFavor usar uma idade maior ou igual a 18 anos\033[m')
                    while True:
                        global email
                        try:
                            email = converte_numero(input('Digite o seu melhor email: \033[33m'))
                            print('\033[m', end='')
                            st('cls')
                            if len(email) > 6 and (email != email01):
                                break
                        except (TypeError, ValueError):
                            print('Digite um email maior que 6 caracteres e um email diferente do já criado')
                        else:
                            # pass
                            print('Digite um email maior que 6 caracteres')
                        finally:
                            # print('Ótimo email')
                            sp(1)
                            st('cls')
                            print('Continuando...')
                            sp(1)
                            st('cls')
                    # email = str(input('Digite o seu melhor email: \033[33m'))
                    print('\033[m', end='')


                    #---------------#
                    # FUNÇÕES MENUS #
                    #---------------#
                    def menu():
                        print()
                        print('''[1] criar uma senha: 
[2] gerar senha: ''')
                    while True:
                        try:
                            menu()
                            opcao = int(input('Escolha sua opção: \033[33m'))
                            print('\033[m', end='')
                            st('cls')
                            if opcao > 0:
                                break
                        except (ValueError, TypeError):
                            print('Erro, digite uma opção válida')
                            menu()
                            sp(0.7)
                            st('cls')
                            continue
                        else:
                            print('Nenhum erro')
                    st('cls')
                    if opcao == 1:
                        senha01 = converte_numero(input('Digite uma senha: \033[7;30m'))
                        # senha01 = int(input('Digite uma senha de números: \033[7;30m'))
                        print('\033[m', end='')
                        while True:
                            try:
                                senha02 = converte_numero(input('Digite uma senha: \033[7;30m'))
                                print('\033[m', end='')
                                sp(1)
                                st('cls')
                                print('Conta criada')
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


                        #-------------#
                        # FUNÇÃO MENU #
                        #-------------#
                        def MENU():
                            #--------------------#
                            # CORPO DO DOCUMENTO #
                            #--------------------#
                            print()
                            print("-------------------------")
                            print("GERADOR DE SENHAS PASSRAP")
                            print("-------------------------")
                            print("Info: Este programa irá gerar uma senha para ser utilizada em cadastros e contas!")
                            print()
                        MENU()
                        while True:
                            nome1 = input("Digite o nome de usuário: \033[33m")
                            print('\033[m', end='')
                            st('cls')
                            MENU()
                            if nome1 != usuario:
                                break
                        print('\033[m', end='')
                        quantidade = converte_numero(input("Digite a quantidade de caracteres que deseja ter na senha: "))
                        pergunta_link = converte_numero(input("Quer digitar o link do site? sim/não: "))
                        pergunta_link, link = gerador.pergunta_link(pergunta_link) # usa duas variaveis para salvar os dois valores retornados pelo return da função
                        #-------------------#
                        # GERADOR DE SENHAS #
                        #-------------------#
                        senha03 = gerador.gerador_senha(quantidade)
                        print("SUA SENHA É: {}".format(senha))
                        print()
                        pergunta = input("Deseja salvar em um arquivo? sim/não: \033[33m")
                        print('\033[m', end='')
                        pergunta = gerador.pergunta_arquivo(pergunta)
            except:
                pass
                # print('ERRO!!!')
            else:
                print('Conta criada com sucesso!')
            finally:
                conta_criada += 1
            # print('Conta criada com sucesso!')
            if criar in 'Nn':
                break


    #--------------#
    # FUNÇÃO LOGIN #
    #--------------#
    def login (n, s):
        global nome
        global senha
        sistema_banco_de_dados(usuario, senha1)
        while True:
            try:
                nome = converte_numero(input('Nome: \033[33m'))
                # nome = str(input('Nome: \033[33m'))
                print('\033[m', end='')
                if nome:
                    break
            except:
                print('ERRO!!!')
        while True:
            try:
                # if senha.isdigit()
                senha = converte_numero(input('Senha: \033[7;30m'))
                # senha = str(input('Senha: \033[7;30m')).strip().capitalize()
                print('\033[m', end='')
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


    #-----------------------#
    # FUNÇÃO BANCO DE DADOS #
    #-----------------------#
    def sistema_banco_de_dados (u, s):
        global usuario
        global senha1
        global email01
        usuario = converte_numero('estevam@sl_2019')
        # usuario = 'estevam@sl_2019'
        # senha1 =  'Respira123'
        senha1 = converte_numero('Respira123')
        email01 = converte_numero('estevamsouzalaureth@gmail.com')


    #------------------#
    # FUNÇÃO CONTINUAR #
    #------------------#
    def continuar ():
        while True:
            login(usuario, senha1)
            resposta = ' '
            resposta = str(input('Deseja continuar [S/N]: \033[33m')).strip().title()
            print('\033[m', end='')
            st('cls')
            while resposta not in 'SsNn':
                resposta = str(input('\033[31mERRO!!! Digite novamente, para continuar [S/N]:\033[m \033[31m')).strip().title()
                print('\033[m', end='')
                st('cls')
            if resposta in 'Nn':
                break
    continuar()
    print(f'Foi {conta_criada} contas criadas')
projeto()
