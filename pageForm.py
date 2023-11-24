import cherrypy
from classes.aluno import * # ou from classes.especie import0 *

class PaginaForm():
    topo = open("html/header.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()
    
    def montaFormulario(self, pId=0, txtId='',tnome='', temail='', telefone=''):
        str = self.topo
        str += '''
            <section class="programacao-box-cards inscricao" id="inscricao">

                    <head class="program-container center">

                        <div class="program-container flex-column center">
                        <div class="cards-container">
                            <h1 class="title-box-program">Faça já sua inscrição!</h1>
                            <div class="card__enrollment">
                            <div class="program-card__enrollment card1__enrollment">
                                <div class="content-box-card__enrollment">
                                <div class="content-descr-card__enrollment">
                                    <p class="card-content__enrollment">

                                    <form name="Cadastro" action="" method="post"><br /><br />
                                        <ul class="list-program">

                                            <input type="hidden" id="txtId" name="txtId" value="%s"/>
                                            
                                            <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                <a class="program-link   font-size__enrollment">
                                                <label class="font-size__enrollment" for="tnome">Nome:</label>
                                                <input type="text" id="tnome" name="tnome" size="30rem" maxlength="55"
                                                placeholder="Digite seu nome" required="required" value="%s" /></a>
                                            </li>

                                            <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                <a class="program-link   font-size__enrollment"><label for="temail">E-mail:</label>
                                                <input type="email" id="temail" name="temail" size="30rem" maxlength="55"
                                                placeholder="Digite seu E-mail" required="required" value="%s"/></a>
                                            </li>

                                            <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                <a class="program-link   font-size__enrollment"><label for="temail">Senha: </label>
                                                <input type="password" id="tsenha" name="tsenha" size="30rem" maxlength="10"
                                                placeholder="Digite sua senha" required="required" value="%s"/></a>
                                            </li>

                                            <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                <a class="program-link   font-size__enrollment"><label for="telefone">Telefone:</label>
                                                <input type="tel" id="telefone" title="99111-1111" placeholder="Digite seu telefone" value="%s"></a>
                                            </li>

                                            <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                <a class="program-link   font-size__enrollment"><label for="tnome">Curso:</label>
                                                </a>
                                                <select name=“selOpcao” class="checkboxx">
                                                    <option value=“1” selected=“selected”> Sistemas de Informação </option>
                                                    <option value=“2”> Ciência da Computação </option>
                                                    <option value=“3”> Engenharia de Software </option>
                                                    <option value=“4”> Análise e Desenvolvimento de Sistemas </option>
                                                    <option value=“5”> Outros </option>
                                                </select>
                                            </li>
                                            <br>

                                            <div class="botoes">
                                                <input class="botao" id="bmensagem" type="submit" name="bmensagem" value="OK" />
                                                <input class="botao" type="reset" name="blimpar" value="LIMPAR" />
                                            </div>

                                        </ul>
                                    <br>
                                </div>
                                </form>
                                </p>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>

                        <br /><br />
                    </head>
                </section>
                ''' % (pId,txtId,tnome,temail,telefone)

        str += self.montaTabela()
        return str

    def montaTabela(self):
        html = '''<table>
                     <tr> 
                        <th> Código </th>
                        <th> Nome </th>
                        <th> Email </th>
                        <th> Telefone </th>      
                     </tr> '''
        # buscar os dados do banco de dados
        objAluno = Aluno() # criamos um objeto do tipo Especie
        dados = objAluno.obterEspecies() # será criada uma lista com o resultado o SQL
        for linha in dados:
            html += ''' <tr>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td style="text-align:center;"> 
                              <a href="excluirEspecie?idEsp=%s">[Excluir]</a>
                              <a href="alterarEspecie?idEsp=%s">[Alterar]</a>
                           </td>
                        </tr> ''' % (linha['esp_id'], linha['esp_descricao'],linha['esp_origem'],linha['esp_id'],linha['esp_id'])
        html +=''' </table> <br> <br>'''
        return html
    

    @cherrypy.expose()
    def gravarAluno(self,txtId,tnome,temail,telefone):

        if len(tnome) > 0: ## eu coloquei verificacoes na classe e 
            #percebi que nao sei lidar com os erros se o retorno for invalido, entao é melhor
            #portar as condicoes de lá nesse módulo aqui
            #antes de escrever no objeto!! 

            # fazer os procedimentos para gravar
            objAluno = Aluno()
            objAluno.set_name(tnome)
            objAluno.set_email(temail)
            objAluno.set_tel(telefone)

            # objAluno curso = int
            # objAluno isActive = True   -> ainda nao os fiz 
            # self.__sendInfo = bool


                ###parei aqui
            # se o txtId = 0, representa que estamos inserindo uma nova espécie
            retorno = 0
            if int(txtId) == 0: # nova espécie
                retorno = objAluno.gravar()
            if retorno > 0:
                return '''
                        <script>
                           alert(" A aluno %s foi gravado com sucesso!!")
                           window.location.href = "/form"
                        </script>
                       ''' % (tnome)
            else: # if retorno > 0:  - Quer dizer que deu erro na hora de gravar
                return '''
                        <h2> Erro ao gravar o aluno %s</h2>
                        <a href="/form">voltar</a>
                        ''' % (tnome)
        else: # len(txtDescr) > 0:
            return '''
                   <h2> O nome do aluno deve ser informado</h2>
                   <a href="/form">Voltar</a>
               '''