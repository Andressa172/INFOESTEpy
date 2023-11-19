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

class Aluno:
    def __init__(self):
          self.__dataobj = Data()
    
    def setData(self, dia, mes, ano):
        self.__dataobj.set_dataNascimento(dia, mes, ano)

    def getData(self):
        return self.__dataobj.__str__()

aluno = Aluno()
aluno.setData(1,10,2013)
print("A data de nascimento do aluno é ", aluno.getData())