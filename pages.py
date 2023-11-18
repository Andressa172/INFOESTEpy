import cherrypy

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
    
class PaginaLivia():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("PortfolioLivia/index.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.body

        return html

class PaginaMaratona():

    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/maratona.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html