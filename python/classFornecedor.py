import json
import tempfile
import shutil
from classPessoa import Pessoa


class Fornecedor(Pessoa):
    
    #feito
    def __init__(self,nome,telefone,email,produtos=[]):
        #Nome através de herança da classe Pessoa
        super().__init__(nome)
        
        self.__telefoneFornecedor = telefone
        self.__email = email
        self.__produtos = produtos
        
        dadosFornecedor = {'telefone':self.getTelefone(), 'email':self.getEmail(), 'produtos':self.getProdutos()}
        loginPadrao = {'senha':None}
        
        with open('arquivos\cadastroFornecedor.json','r') as arquivoCadastroFornecedores,\
            open('arquivos\\fornecedor.json','r') as arquivoFornecedores,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempFornecedores,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempCadastroFornecedores:
            
                fornecedores = json.load(arquivoCadastroFornecedores)
                loginFornecedores = json.load(arquivoFornecedores)
            
                if not fornecedores:
                    #verifica se já existe fornecedor com esse nome
                    if self.getNome() not in fornecedores:
                        novoFornecedor = {}
                        novoFornecedor[self.getNome()] = dadosFornecedor
                        json.dump(novoFornecedor,tempCadastroFornecedores,ensure_ascii=False,indent=4)
                    else:
                        print('Fornecedor já existente')
                    
                else:
                    fornecedores[self.getNome()] = dadosFornecedor
                    json.dump(fornecedores,tempCadastroFornecedores,ensure_ascii=False,indent=4)
                
                
                if not loginFornecedores:
                    
                    if self.getNome() not in loginFornecedores:
                        loginFornecedores[self.getNome()] = loginPadrao
                        json.dump(loginFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                    
                    else:
                        print('Fornecedor já cadastrado')
                    
                
                else:
                    loginFornecedores[self.getNome()] = loginPadrao
                    json.dump(loginFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
            
        
        shutil.move(tempCadastroFornecedores.name,'arquivos\cadastroFornecedor.json')
        shutil.move(tempFornecedores.name,'arquivos\\fornecedor.json')
    #feito
    def getNome(self):
        
        return Pessoa.getNome()
    #feito 
    def getEmail(self):
    
        return self.__email
    #feito
    def setEmail(self,emailAlterado):
        
        self.__email = emailAlterado
    #feito
    def getTelefone(self):
        
        return self.__telefoneFornecedor
    #feito
    def setTelefone(self,telefoneAlterado):
        
        self.__telefoneFornecedor = telefoneAlterado
    #feito
    def getProdutos(self):
        
        return self.__produtos
    #feito
    def setProdutos(self,novosProdutos=[]):
        
        self.__produtos = novosProdutos
    
    #feito
    def getInfo(self):
        
        print('Nome do fornecedor:',self.getNome())
        print('Email:',self.getEmail())
        print('Telefone:',self.getTelefone())
        print('Produtos:',self.getProdutos())
             
                
            
            
    #Métodos de pesquisa fora da classe

    def getInfoFornecedor(nome):
            
        with open('arquivos\cadastroFornecedor.json','r') as arquivo:

            conteudoArquivo = json.load(arquivo)
        
            if nome in conteudoArquivo:
                print(f'Fornecedor:',nome)
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
    def setProdutosFornecedor(nome):
        
        with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
            tempfile.NamedTemporaryFile('w',delete=False) as alteraProduto:
                
                conteudoArquivo = json.load(arquivo)
                
                novosItens = []
                
                if nome in conteudoArquivo:
                    
                    while True:
                    
                        novoItem = input('Insira o item a ser adicionado:')

                        if novoItem not in conteudoArquivo[nome]["produtos"]:
                            conteudoArquivo[nome]["produtos"].append(novoItem)
                    
                    
                        print('0 - Parar inserção de novo item fornecido')
                        print('1 - Adicionar novo item')
                                    
                        escolhaCont = input('Escolha a opção desejada:')
                                    
                        print('*************************************************')
                                    
                        if escolhaCont == "0":
                            print("Encerrando")
                            break
                        
                        print('*************************************************')
                        
                    
                    json.dump(conteudoArquivo,alteraProduto,ensure_ascii=False,indent=4)
                
                else:
                    print('Não existe fornecedor com esse nome')
                
        shutil.move(alteraProduto.name,'arquivos\cadastroFornecedor.json')
                    

    def removeItem(nome,item):

        with open('arquivos\cadastroFornecedor.json','r') as arquivo,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempArquivo:
                
            conteudoArquivo = json.load(arquivo)
            
            if item in conteudoArquivo[nome]["produtos"]:
                
                conteudoArquivo[nome]["produtos"].remove(item)
                json.dump(conteudoArquivo,tempArquivo,ensure_ascii=False,indent=4)
                shutil.move(tempArquivo.name,'arquivos\cadastroFornecedor.json')
            
            else:
                print('O fornecedor não apresenta esse produto como opção')

            
    def listaPedidosForn(nomeFornecedor):
        
        with open('arquivos\pedidos.json','r') as arquivoPedidos:
            
            conteudoArquivo = json.load(arquivoPedidos)
            
            chaves = conteudoArquivo.keys()
            
            cont = 0
            
            
            for chave in chaves:
                
                if conteudoArquivo[chave]["fornecedor"] == nomeFornecedor:
                    print('*************************************************')
                    print('Número do Pedido:',chave)
                    print('Itens:',conteudoArquivo[chave]["itens"])
                    cont += 1
                else:
                    pass
                
            if cont == 0:
                print('O fornecedor não possui pedido')
                
                
            
            
                    
                

                
            
            
                