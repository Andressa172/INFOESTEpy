import cherrypy
import os
from pages import *

local_dir = os.path.dirname(__file__)

#run
index()

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
    }
}



#objetos utilizados para rota de navegação
root = index() #rota principal
root.sobre = PaginaAbout()
root.ciclodecursos = PaginaCursos()
root.fippetec = PaginaEtec()
root.festalinux = PaginaLinux()
root.maratonadeprogramacao = PaginaMaratona()


cherrypy.quickstart(root,config=local_config)
