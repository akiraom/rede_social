class Cadastro:
    user = []
    def __init__(self, nome, idade, user, senha):
        self.nome = nome
        self.idade = idade
        self.user = user
        self.senha = senha
        Cadastro.user.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.user} | {self.senha}'
    
    @classmethod
    def listar_user(cls):
        print(f'{'Nome'.ljust(20)} | {'Idade'.ljust(20)} | {'Nome do Usuario'.ljust(20)} | {'Senha'}')
        for usuario in cls.user:
            print(f'{usuario.nome.ljust(20)} | {str(usuario.idade).ljust(20)} | {usuario.user.ljust(20)} | {usuario.senha}')


    def alterar_user(self, novo_user = None):
        self.user = novo_user
        print('Nome de usuário alterado com sucesso')
    def alterar_senha(self, nova_senha = None):
        self.senha = nova_senha
        print('Senha alterada com sucesso')
       
class Mensagens:
    mensagens = []
    def __init__(self, user, mensagem):
        self.mensagens = mensagem
        self.user = user
        Mensagens.mensagens.append(self)

    def __str__ (self):
        return f'{self.user}: {self.mensagens}'
    
    @classmethod
    def ver_mensagens(cls):
        print('Lista de mensagens\n')
        for msg in cls.mensagens:
            print(f'{msg.user}: {msg.mensagens}')
