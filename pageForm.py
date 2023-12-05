import cherrypy
from classes.aluno import *

class PaginaForm():

    header = open("html/headerForm.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self, txtId=None, tnome=None, temail=None, telefone=None, selOpcao=None, bgravar=None):
        return self.montaFormulario()

    def montaFormulario(self, pId=0, tnome='', temail='', telefone='', selOpcao=1):
        str = self.header
        str += '''
        <section class="programacao-box-cards inscricao" id="inscricao">

            <head class="program-container center">

                <div class="program-container flex-column center">
                    <div class="cards-container-inscricao">
                        <h1 class="title-box-program">Faça já sua inscrição!</h1>
                        <div class="card__enrollment">
                            <div class="program-card__enrollment card1__enrollment">
                                <div class="content-box-card__enrollment">
                                    <div class="content-descr-card__enrollment">
                                        <p class="card-content__enrollment">

                                            <form name="Cadastro" action="" method="post"><br /><br />
                                                <input type="hidden" id="txtId" name="txtId" value="{}"/>
                                                <ul class="list-program">
                                                    <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                        <a class="program-link   font-size__enrollment"><label class="font-size__enrollment"
                                                            for="tnome">Nome:</label>
                                                        <input type="text" id="tnome" name="tnome" size="30rem" maxlength="55"
                                                            placeholder="Digite seu nome" required="required" value="{}" /></a>
                                                    </li>

                                                    <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                        <a class="program-link   font-size__enrollment"><label for="temail">E-mail:</label>
                                                        <input type="email" id="temail" name="temail" size="30rem" maxlength="55"
                                                            placeholder="Digite seu E-mail" required="required" value="{}"/></a>
                                                    </li>

                                                    <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                        <a class="program-link   font-size__enrollment"><label for="telefone">Telefone:</label>
                                                        <input type="tel" id="telefone" title="99111-1111"
                                                            placeholder="Digite seu telefone" value="{}"></a>

                                                    </li>

                                                    <li class="program-item inscr "><img src="../imgs/seta.png" alt="ícone seta" class="seta-list">
                                                        <a class="program-link   font-size__enrollment"><label for="tnome">Curso:</label>
                                                        </a>
                                                        <select name="selOpcao" class="checkboxx">
                                                            <option value="1" selected="selected"> Sistemas de Informação </option>
                                                            <option value="2"> Ciência da Computação </option>
                                                            <option value="3"> Engenharia de Software </option>
                                                            <option value="4"> Análise e Desenvolvimento de Sistemas </option>
                                                            <option value="5"> Outros </option>
                                                        </select>
                                                    </li><br>


                                                    

                                                    <br />

                                                    <div class="botoes">
                                                        <input class="botao" type="submit" name="bgravar" id="bgravar" value="OK" />
                                                        <input class="botao" type="reset" name="blimpar" value="LIMPAR" />
                                                    </div>
                                                </ul>
                                                <br>

                                            </form>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <br /><br />
            </head>
        </section>
        '''.format(pId, tnome, temail, telefone, selOpcao)

        str += self.montaTabela()
        return str

    def montaTabela(self):
        html = '''  
                    <section class="section-table">
                        <h1 class="title-box-program">Dados cadastrados</h1>
                        <table class="tabela">
                            <tr> 
                                <th> Código </th>
                                <th> Nome </th>
                                <th> Email </th>
                                <th> Telefone </th>      
                                <th> Curso </th>      
                            </tr> 
                    </section>
                '''
        
        # buscar os dados do banco de dados
        objAluno = Aluno() # criamos um objeto do tipo Aluno
        dados = objAluno.obterAluno() # será criada uma lista com o resultado o SQL
        
        for linha in dados:
            html += ''' <tr>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td style="text-align:center;"> 
                              <a href="excluirAluno?idAluno=%s">[Excluir]</a>
                              <a href="alterarAluno?idAluno=%s">[Alterar]</a>
                           </td>
                        </tr> ''' % (linha['aluno_id'], linha['aluno_nome'],linha['aluno_email'],linha['aluno_tel'],linha['aluno_curso'],linha['aluno_id'],linha['aluno_id'])
        html +=''' </table> <br> <br>'''
        return html
    
    @cherrypy.expose()
    def gravarAluno(self, txtId, tnome, temail, telefone, selOpcao, bgravar): # vai ser chamado quando clicar no botão
        if len(tnome) > 0:
            # fazer os procedimentos para gravar
            objAluno = Aluno()
            objAluno.set_nome(tnome)
            objAluno.set_email(temail)
            objAluno.set_tel(telefone)
            objAluno.set_curso(selOpcao)
            # se o txtId = 0, representa que estamos inserindo uma nova espécie
            retorno = 0
            if int(txtId) == 0: # nova espécie
                retorno = objAluno.gravar()
            else: # vai gravar uma alteração no banco de dados
                objAluno.set_id(int(txtId))
                retorno = objAluno.alterar()
            if retorno > 0:
                return '''
                        <script>
                           alert("O aluno %s foi gravado com sucesso!!")
                           window.location.href = "/rotaAluno"
                        </script>
                       ''' % (tnome)
            else: # if retorno > 0:  - Quer dizer que deu erro na hora de gravar
                return '''
                        <h2> Erro ao gravar o aluno %s</h2>
                        <a href="/rotaAluno">voltar</a>
                        ''' % (tnome)
        else: # len(txtDescr) > 0:
            return '''
                   <h2> O nome do aluno deve ser informado</h2>
                   <a href="/rotaAluno">voltar</a>
               '''
    
    @cherrypy.expose()
    def excluirAluno(self,idAluno):
        objAluno = Aluno()
        objAluno.set_id(int(idAluno))
        if objAluno.excluir() > 0: # informa se conseguiu excluir ou não
            raise cherrypy.HTTPRedirect('/rotaAluno') # para atualizar a página após a exclusão (tipo reload)
        else:
            return '''
            <h2>Não foi possível excluir o aluno!!</h2>
            [<a href="/rotaAluno">Voltar</a>]
            '''

    @cherrypy.expose()
    def alterarAluno(self,idAluno):
        objAluno = Aluno()
        # buscar no banco a espécie que foi informada no parâmetro
        dadosAlunoSelec = objAluno.obterAluno(idAluno)
        # chamar o método para montar o formulário com os dados da espécie selecionada na tabela e carregar nos elementos <input> do formulário
        return self.montaFormulario(dadosAlunoSelec[0]['aluno_id'],
                                    dadosAlunoSelec[0]['aluno_nome'],
                                    dadosAlunoSelec[0]['aluno_email'],
                                    dadosAlunoSelec[0]['aluno_tel'],
                                    dadosAlunoSelec[0]['aluno_curso']
                                    )
                                    