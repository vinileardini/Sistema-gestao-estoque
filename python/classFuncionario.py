from classPessoa import Pessoa
import tempfile
import json
import shutil

class Funcionario(Pessoa):
    
    def __init__(self,nome,registro):
        super().__init__(nome)
        
        self.registro = registro


        with open('arquivos\\usuario.json','r') as arqFuncionario,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempFunc:
                
                conteudoArq = json.load(arqFuncionario)
                
                if self.getNome() not in conteudoArq:
                    
                    while True:
                        
                        cadastSenha = input('Defina a senha para o usuário:')
                        repeteSenha = input('Insira novamente a senha:')
                        
                        if cadastSenha == repeteSenha:
                            dadosUser = {"senha":cadastSenha}
                            conteudoArq[self.getNome()] = dadosUser
                            json.dump(conteudoArq,tempFunc,ensure_ascii=False,indent=4)
                            print('Funcionario cadastrado')
                            break
                        
                        else:
                            print('As senhas informadas são diferentes')
                
                else:
                    print('Funcionário já cadastrado')
                        
        shutil.move(tempFunc.name,'arquivos\\usuario.json') 
            
    def getNome(self):
        
        return self.nome
    

