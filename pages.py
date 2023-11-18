import cherrypy

header = open("html/header.html", encoding="utf-8").read()

class PaginaAbout():
    principal = open("html/pageSobre.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.principal

        return html
    
class PaginaCursos():
    principal = topo = open("html/ciclodecursos.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.principal

        return html
    
class PaginaEtec():
    principal = topo = open("html/fippetec.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.principal

        return html

class PaginaLinux():
    principal = open("html/festalinux.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.principal

        return html
    
class PaginaLivia():
    principal = open("PortfolioLivia/index.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.principal

        return html

class PaginaMaratona():

    principal = topo = open("html/maratona.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.principal

        return html