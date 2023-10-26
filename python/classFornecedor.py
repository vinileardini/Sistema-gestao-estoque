import json
import tempfile
import shutil


class Fornecedor:
    
    def __init__(self,nome,telefone,email,produtos=[]):
        
        self.nomeFornecedor = nome
        self.telefoneFornecedor = telefone
        self.email = email
        self.produtos = produtos
        
    #Feito
    def cadastrarFornecedor(self):
        
        dadosFornecedor = {'telefone':self.telefoneFornecedor, 'email':self.email, 'produtos':self.produtos}
        
        with open('arquivos\cadastroFornecedor.json','r') as arquivoFornecedores,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempFornecedores:
            
            fornecedores = json.load(arquivoFornecedores)
            
            if not fornecedores:
                #verifica se já existe fornecedor com esse nome
                if self.nomeFornecedor not in fornecedores:
                    novoFornecedor = {}
                    novoFornecedor[self.nomeFornecedor] = dadosFornecedor
                    json.dump(novoFornecedor,tempFornecedores,ensure_ascii=False,indent=4)
                else:
                    print('Fornecedor já existente')
                
            else:
                fornecedores[self.nomeFornecedor] = dadosFornecedor
                json.dump(fornecedores,tempFornecedores,ensure_ascii=False,indent=4)
        
        shutil.move(tempFornecedores.name,'arquivos\cadastroFornecedor.json')
                
                
                
                
#Feito
def getNome(nome):
        
        with open('arquivos\cadastroFornecedor.json','r') as arquivo:
        
            conteudoArquivo = json.load(arquivo)
        
            if nome in conteudoArquivo:
                print(f'O fornecedor {nome} foi encontrado')
                print('Email para contato:',conteudoArquivo[nome]["email"])
                print('Telefone:',conteudoArquivo[nome]["telefone"])
                print('Produtos oferecidos:',conteudoArquivo[nome]["produtos"])
            
            else:
                print('Não existe fornecedor com esse nome')
    



def setEmailFornecedor(nome,novoEmail):
    
    with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as alteracaoEmail:
            
        conteudoArquivo = json.load(arquivo)
    
        if nome in conteudoArquivo:
            conteudoArquivo[nome]["email"] = novoEmail
    
        else:
            print('Não existe fornecedor com esse nome')   
            
    shutil.move(alteracaoEmail.name,'arquivos\cadastroFornecedor.json') 

def setTelefoneFornecedor(self,novoTelefone):
    
    self.telefoneFornecedor = novoTelefone

    
        
        