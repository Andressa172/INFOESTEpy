#ID, Nome, Email, Telefone, Data de nascimento, endereco completo, curso, foto, notificacoes, isActive, sendInfo
from classes.banco import *

class Aluno:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__tel = ''
        self.__email = ''
        self.__endereco = ''
        self.__senha = ''
        self.__curso = 0
        self.__bd = Banco()

        def set_id(self, id): 
            if id > 0:
                self.__id = id
        
        def set_name(self, name):
            self.__name = name

        def set_tel(self, tel):
            self.__tel = tel

        def set_email(self, email):
            self.__email = email
        
        def set_endereco(self, endereco):
               self.__endereco = endereco
        
        def set_curso(self, curso):
            self.__curso = curso
        
        def set_senha(self, senha):
            self.__senha = senha

        def write(self): # vai pegar os dados do objeto e gravar na tabela do banco
            sql = ''' INSERT INTO alunos (nome,telefone,aniversario,endereco,curso,notificacoes)
                    values ("#nome", "#telefone", #aniversario, #endereco, #curso, #notificacoes)
                '''
            sql = sql.replace('#nome',self.__name)
            sql = sql.replace('#telefone', self.__tel)
            sql = sql.replace('#aniversario', self.__dn)
            sql = sql.replace('#endereco', self.__endereco)
            sql = sql.replace('#curso', self.__curso)
            sql = sql.replace('#notificacoes', self.__sendInfo)
            return self.__banco.runCRUD(sql)