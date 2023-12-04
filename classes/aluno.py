from classes.banco import Banco

class Aluno(): # está é o nome da classe de Espécies
    '''
        Documentação da classe
        - aqui nó vamos descrever os campos (propriedades) e funções (métodos) para definirmos de acordo com a teoria de Programação Orientada a Objetos
    '''
    # Construtor
    def __init__(self):
        # propriedades privadas
        self.__id = 0
        self.__nome = ''
        self.__email = ''
        self.__tel = ''
        self.__curso = 1
        self.__banco = Banco() # aqui será criado o objeto que representa o acesso ao Banco de Dados, nós iremos utilizar ela para gravar, excluir, alterar e buscar os dados já gravados no banco
        # propriedades públicas

    # definir os métodos para a nossa classe para colocar os valores nas propriedades
    def set_id(self, pId): # setar o valor é autoincremento
        if pId > 0: # validação dos valores para não serem negativos ou zerados, e serem corretamente associados à propriedade
            self.__id = pId
    def set_nome(self,tnome):
        if len(tnome) > 0:
            self.__nome = tnome

    def set_email(self,temail):
        self.__email = temail

    def set_tel(self,telefone):
        self.__tel = telefone

    def set_curso(self,selOpcao):
        self.__curso = selOpcao

    # métodos para obter os valores das propriedades
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_tel(self):
        return self.__tel
    
    def get_curso(self):
        return self.__curso

    # devolver todas as espécies cadastradas no banco de dados na tabela Especies
    def obterAluno(self):
        sql = '''
              SELECT aluno_id, aluno_nome, aluno_email, aluno_tel, aluno_curso
              FROM Aluno
              ORDER by aluno_nome
              '''
        return self.__banco.executarSelect(sql)

    def gravar(self): # vai pegar os dados do objeto e gravar na tabela do banco
        sql = ''' INSERT INTO Aluno (aluno_nome,aluno_email,aluno_tel,aluno_curso)
                 values ("#nome", "#email", "#tel", "#curso")
              '''
        sql = sql.replace('#nome',self.__nome)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#tel', self.__tel)
        sql = sql.replace('#curso', self.__curso)
        return self.__banco.executarInsertUpdateDelete(sql)

    # devolver uma espécia só cdastrada no banco de dados na tabela Especies
    def obterAluno(self, pId=0):
        if pId != 0:
            self.__id = pId
        sql = ''' SELECT aluno_id, aluno_nome, aluno_email, aluno_tel, aluno_curso
                  FROM Aluno
                  where aluno_id = #id         '''
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def excluir(self):
        sql = 'delete from Aluno where aluno_id = #id'
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = 'update Aluno set aluno_nome = "#nome", aluno_email = "#email", aluno_tel = "#tel", aluno_curso =  "#curso" where aluno_id = #id'
        sql = sql.replace('#nome',self.__nome)
        sql = sql.replace('#email',self.__email)
        sql = sql.replace('#tel',self.__tel)
        sql = sql.replace('#curso',self.__curso)
        sql = sql.replace('#id',str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)
