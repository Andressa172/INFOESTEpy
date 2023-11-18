import cherrypy
import os
from pages import *

local_dir = os.path.dirname(__file__)

class index():
    header = open("html/header.html", encoding="utf-8").read()
    principal = open("html/index.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.principal
        return html

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 80
}
cherrypy.config.update(server_config)

#Para que o cherrypy possa encontrar os arquivos dentro do diretório da aplicação
local_config = {
    "/": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": local_dir,
    },
    "/#": {
        "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
    },
    "/PortfólioLívia": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": os.path.join(os.path.dirname(__file__), "PortfólioLívia"),
    }
}



#objetos utilizados para rota de navegação
root = index() #rota principal
root.rotaAbout = PaginaAbout()
root.rotaCursos = PaginaCursos()
root.rotaEtec = PaginaEtec()
root.rotaLinux = PaginaLinux()
root.rotaMaratona = PaginaMaratona()
root.rotaLivia = PaginaLivia()

cherrypy.quickstart(root,config=local_config)
