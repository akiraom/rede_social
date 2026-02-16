import os
from classe.classes import Cadastro
from classe.classes import Mensagens
cdstr = None
mensagem = ''
def erro_log():
    #Mensagem quando ocorrer erro no login
    print('usuário ou senha não encontrado por favor tente novamente\n')
    input('digite qualquer tecla para tentar novamente\n')
    login()
def limpar(text):
    #Limpa o terminal e deixa uma mensagem se necessário
    os.system('cls')
    print(text)
    print()
def invalido():
    #Mensagem quando acontece algo de errado
    limpar('Opção Inválida, por favor escreva uma opção compatível')
def login():
    '''Função para logar o usuário
    inputs:
        user_log = pede seu nome de usuário
        user_pass = pede sua senha
    '''
    limpar('Login')
    global cdstr
    try:
        user_log = input('Digite seu usuário: ')
        user_encontrado = False
        for log in Cadastro.user:
            if user_log == log.user:
                user_encontrado = True
                user_pass = input('Digite a senha: ')
                if user_pass == log.senha:
                    print('login efetuado com sucesso!!')
                    cdstr = log
                    acesso()
                else:
                    print('Senha incorreta')
                    break
        if not user_encontrado:
                erro_log()
    except:
        invalido()
        login()
def cadastro():
    '''função para cadastrar o usuário na rede:
    inputs: 
        idade
        nome
        usuario
        senha
    '''
    limpar('Cadastro')
    global cdstr
    try:
        idade=int(input('Qual sua idade: '))
        if idade >= 12:
            nome=input('Qual seu nome: ')
            usuario=input('Qual o nome do seu usuário: ')
            senha=input('Qual a senha que deseja usar: ')
            cdstr = Cadastro(nome, idade, usuario, senha)
            limpar('Usuário cadastrado com sucesso')
            inicio()
        else:
            limpar('Você não tem idade para criar a conta')
    except:
        invalido()
        cadastro()
def inicio():
    '''Tela inicial do programa define para onde o usuário deve ir
    inputs:
        sel - serve para selecionar para onde o usuário deseja ir
    '''
    try:
        print('Bem Vindos a Rede Akira\n1. Login\n2. Cadastro')
        sel=int(input('Selecione uma opção: '))
        match sel:
            case 1:
                login()
            case 2:
                cadastro()
            case 3:
                Cadastro.listar_user()
                input('aperte qualquer tecla para voltar')
                os.system('cls')
                inicio()
            case _:
                invalido()
                inicio()
    except:
        invalido()
        inicio()
def publicar_mensagens():
    '''sistema para publicar mensagem, ele pega o nome de usuário e um texto e publica
    input:
        msg = serve para escrever a mensagem que deve ser publicada         
    '''
    os.system('cls')
    msg = input('Digite sua mensagem: ')
    global cdstr
    user = cdstr.user
    mensagem = Mensagens(user, msg)
    print('Mensagem enviada com êxito')
    acesso()
def alterar_dados():
    '''sistema de alteração de dados do usuário como nome de usuário e senha
        inputs:
            dados - serve para informar o que deseja alterar
            n_user - serve para escrever o novo nome de usuário
            n_senha - serve para escrever a nova senha do usuário

    '''
    print('1. Usuario\n2. Senha')
    dados = int(input('Escolha o que deseja alterar: '))
    global login
    if dados == 1:
        n_user = input('Digite seu novo nome de usuário: ')
        cdstr.alterar_user(n_user)
        limpar('')
        inicio()
    elif dados == 2:
        n_senha = input('Digite sua nova senha: ')
        cdstr.alterar_senha(n_senha)
        limpar('')
        inicio()
    else:
        invalido()
        alterar_dados()
def acesso():
        '''Página inicial após o login, serve para direcionar o usuário para onde ele desejar'''
        limpar('Página inicial')
        print('1. Publicar Mensagem\n2. Ver Mensagens\n3. Alterar Dados\n4. Encerrar Sessão')
        try:
            opt=int(input('Selecione uma opção: '))
        
            if opt == 1:
                publicar_mensagens()
            elif opt == 2:
                Mensagens.ver_mensagens()
                input('Digite qualquer tecla para voltar para o ínicio')
                acesso()
            elif opt == 3:
                alterar_dados()
            elif opt == 4:
                limpar('Sessão finalizada, faça o login novamente')
                inicio()
            else:
                invalido()
                acesso()
        except:
            invalido()
            acesso()
def main():
    inicio()
if __name__ == '__main__':
    main()
