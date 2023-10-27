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
def getInfo(nome):
        
        with open('arquivos\cadastroFornecedor.json','r') as arquivo:
        
            conteudoArquivo = json.load(arquivo)
        
            if nome in conteudoArquivo:
                print(f'O fornecedor {nome} foi encontrado')
                print('Email para contato:',conteudoArquivo[nome]["email"])
                print('Telefone:',conteudoArquivo[nome]["telefone"])
                print('Produtos oferecidos:',conteudoArquivo[nome]["produtos"])
            
            else:
                print('Não existe fornecedor com esse nome')
    


#Feito
def setEmailFornecedor(nome,novoEmail):
    
    with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as alteracaoEmail:
            
        conteudoArquivo = json.load(arquivo)
    
        if nome in conteudoArquivo:
            conteudoArquivo[nome]["email"] = novoEmail
            json.dump(conteudoArquivo,alteracaoEmail,ensure_ascii=False,indent=4)
    
        else:
            print('Não existe fornecedor com esse nome')   
            
    shutil.move(alteracaoEmail.name,'arquivos\cadastroFornecedor.json') 

#Feito
def setTelefoneFornecedor(nome,novoTelefone):
    
    with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as alteracaoTelefone:
            
        conteudoArquivo = json.load(arquivo)
        
        if nome in conteudoArquivo:
            conteudoArquivo[nome]["telefone"] = novoTelefone
            json.dump(conteudoArquivo,alteracaoTelefone,ensure_ascii=False,indent=4)
        
        else:
            print('Não existe fornecedor com esse nome')     

    shutil.move(alteracaoTelefone.name,'arquivos\cadastroFornecedor.json')

#Feito
def setProdutosFornecedor(nome,produtos=[]):
    
    with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as alteraProduto:
            
            conteudoArquivo = json.load(arquivo)
            
            if nome in conteudoArquivo:
                conteudoArquivo[nome]["produtos"] = produtos
                json.dump(conteudoArquivo,alteraProduto,ensure_ascii=False,indent=4)
            
            else:
                print('Não existe fornecedor com esse nome')
            
    shutil.move(alteraProduto.name,'arquivos\cadastroFornecedor.json')
                
