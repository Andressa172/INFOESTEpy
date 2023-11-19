import sqlite3


class Banco():
    def __init__(self):#construtor
        self.__conexao = None
        self.__cursor = None

    def __connect(self):
        self.__conexao = sqlite3.connect("bd/alunos.db")
        self.__conexao.row_factory = sqlite3.Row 
        self.__cursor = self.__conexao.cursor()

    def __closeConnection(self):
        self.__cursor.close()
        self.__conexao.close()

    def runCRUD(self, sql):
        linhasAfetadas = -10 
        if len(sql) > 0:
            self.__connect()
            self.__cursor.execute(sql)
            linhasAfetadas = self.__cursor.rowcount 
            self.__conexao.commit()
            self.__closeConnection()
        return linhasAfetadas

    def executarSelect(self, sql):
        dados = ''
        if len(sql) > 0:
            self.__connect()

            self.__cursor.execute(sql)
            dados = self.__cursor.fetchall() 

            self.__closeConnection()
        return dados