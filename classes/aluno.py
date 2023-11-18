#ID, Nome, Email, Telefone, Data de nascimento, endereco completo, curso, foto, notificacoes, isActive, sendInfo
from banco import *

class Data:
    dia: int
    mes: int
    ano: int

class Tel:
    ddd: int
    numero: str


class Aluno:

    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__tel = Tel
        self.__dn = Data
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
            if len(str(tel.numero)) == 9 and isinstance(tel.ddd,int) :
                self.__tel = tel

        def set_dataNascimento(self, data):
            if isinstance(data.dia, int) and data.dia in range(0,31):
                if isinstance(data.mes, int) and data.mes in range(1,12):
                    if isinstance(data.ano, int) and data.ano >= 0:
                        self.__dn = data
        
        def set_endereco(self, endereco):
            if len(endereco)>0:
                self.__endereco = endereco
        
        def set_curso(self, curso):
            if isinstance(curso, int) and curso in range(0,3):
                self.__curso = curso
        
        ###parei aqui 