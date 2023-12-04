import cherrypy
from classes.aluno import *

class index():
    header = open("html/headerIndex.html", encoding="utf-8").read()
    titulo = open("html/titulo.html", encoding="utf-8").read()
    cards = open("html/cards.html", encoding="utf-8").read()
    contact = open("html/contact.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self, id=0, tnome=''):
        html = self.header 
        html += self.titulo
        html += self.cards
        html += self.contact
        return html
    
    # @cherrypy.expose()
    # def gravarAluno(self,tnome,temail,telefone, date, endereco ,btnGravar):

    #     if len(tnome) > 0: ## eu coloquei verificacoes na classe e 
    #         #percebi que nao sei lidar com os erros se o retorno for invalido, entao é melhor
    #         #portar as condicoes de lá nesse módulo aqui
    #         #antes de escrever no objeto!! 

    #         # fazer os procedimentos para gravar
    #         objAluno = Aluno()
    #         objAluno.set_name(tnome)
    #         objAluno.set_email(temail)
    #         objAluno.set_tel(telefone)
    #         objAluno.set_data(date)
    #         objAluno.set_endereco(endereco)

    #         # objAluno curso = int
    #         # objAluno isActive = True   -> ainda nao os fiz 
    #         # self.__sendInfo = bool


    #             ###parei aqui
    #         # se o txtId = 0, representa que estamos inserindo uma nova espécie
    #         retorno = 0
    #         if int(txtId) == 0: # nova espécie
    #             retorno = objAluno.gravar()
    #         if retorno > 0:
    #             return '''
    #                     <script>
    #                        alert(" A espécie %s for gravada com sucesso!!")
    #                        window.location.href = "/rotaEspecie"
    #                     </script>
    #                    ''' % (txtDescr)
    #         else: # if retorno > 0:  - Quer dizer que deu erro na hora de gravar
    #             return '''
    #                     <h2> Erro ao gravar a espécie %s</h2>
    #                     <a href="/rotaEspecie">voltar</a>
    #                     ''' % (txtDescr)
    #     else: # len(txtDescr) > 0:
    #         return '''
    #                <h2> A descrição da espécie deve ser informada</h2>
    #                <a href="/rotaEspecie">voltar</a>
    #            '''

class PaginaAbout():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/pageSobre.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    
class PaginaCursos():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/ciclodecursos.html", encoding="utf-8").read()
    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    
class PaginaEtec():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/fippetec.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html

class PaginaLinux():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/festalinux.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    

class PaginaMaratona():

    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/maratona.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    

