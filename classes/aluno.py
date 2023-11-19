#ID, Nome, Email, Telefone, Data de nascimento, endereco completo, curso, foto, notificacoes, isActive, sendInfo
from banco import *

class Data:
    def __init__(self):
        self.__dia = 1
        self.__mes = 1
        self.__ano = 2000

    def __str__(self):
        return str(self.__dia) + " " + str(self.__mes) + " " + str(self.__ano)
    
    def set_dataNascimento(self, dia, mes, ano):
            if isinstance(dia, int) and dia in range(1,31):
                if isinstance(mes, int) and mes in range(1,12):
                    if isinstance(ano, int) and ano >= 0:
                        self.__dia = dia
                        self.__mes = mes
                        self.__ano = ano

class Tel:
    def __init__(self):
        self.__ddd = ''
        self.__telefone = ''

        def __str__(self):
            return self.__ddd + "-" + self.__telefone
        
        def set_Telefone(self, ddd, telefone):
            if len(ddd) == 2 and len(telefone) == 9:
                self.__ddd = ddd
                self.__telefone = telefone



class Aluno:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__tel = Tel()
        self.__dn = Data()
        self.__endereco = ''
        self.__curso = int
        self.__isActive = True
        self.__sendInfo = bool
        self.__bd = Banco()

        def set_id(self, id): 
            if id > 0:
                self.__id = id
        
        def set_name(self, name):
            if len(name)>0:
                self.__name = name

        def set_tel(self, tel):
            if len(str(tel.numero)) == 9 and isinstance(tel.ddd,int):
                self.__tel = "%d%d"%(Tel.ddd,Tel.numero)

        def set_data(self, dia, mes, ano):
            if isinstance(dia, int) and dia in range(0,31):
                if isinstance(mes, int) and mes in range(1,12):
                    if isinstance(ano, int) and ano >= 0:
                        self.__dn.set_dataNascimento(dia, mes, ano)

        def set_tel (self, ddd, numero):
            if len(str(ddd))==2 and len(str(numero))==9:
                self.__tel.set_Telefone(ddd, numero)
        
        def set_endereco(self, endereco):
            if len(endereco)>0:
                self.__endereco = endereco
        
        def set_curso(self, curso):
            if isinstance(curso, int) and curso in range(0,3):
                self.__curso = curso
        
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