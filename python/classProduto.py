
import tempfile
import shutil
import json


class Produto:
    
    def __init__(self,tipoProduto,marca,categoria,precoCompra,precoVenda,quantidadeProduto):
        
        self.__tipoProduto = tipoProduto
        self.__marca = marca
        self.__categoriaProduto = categoria
        self.__precoCompra = precoCompra
        self.__precoVenda = precoVenda
        self.__quantidade = quantidadeProduto
        
    #Feito
    def adicionarProduto(self,quantidade):
        
        with open('arquivos\estoque.json','r') as arquivo,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempProduto:
                
            conteudoArquivo = json.load(arquivo)
            
            if self.__tipoProduto not in conteudoArquivo:
                
                dadosProduto = {'marca':self.__marca,'categoria':self.__categoriaProduto,'preco_de_compra':self.__precoCompra,'preco_de_venda':self.__precoVenda,'quantidade':self.__quantidade}
                
                conteudoArquivo[self.__tipoProduto] = dadosProduto
                json.dump(conteudoArquivo,tempProduto,ensure_ascii=False,indent=4)
            
            else:
                
                conteudoArquivo[self.__tipoProduto]["quantidade"] += quantidade
                json.dump(conteudoArquivo,tempProduto,ensure_ascii=False,indent=4)
                
        shutil.move(tempProduto.name,'arquivos\estoque.json')
        
    def getTipo(self):
        
        print(self.__tipoProduto)
    
    def setTipo(self,novoTipo):
        
        self.__tipoProduto = novoTipo
    
    def getMarca(self):
        
        print(self.__marca)
    
    def setMarca(self,novaMarca):
        
        self.__marca = novaMarca
    
    def getCategoria(self):
        
        print(self.__categoriaProduto)
        
    def setCategoria(self,novaCategoria):
        
        self.__categoriaProduto = novaCategoria
    
    def getPrecoCompra(self):
        
        print(self.__precoCompra)
    
    def setPrecoCompra(self,novoPrecoC):
        
        self.__precoCompra = novoPrecoC
    
    def getPrecoVenda(self):
        
        print(self.__precoVenda)
    
    def setPrecoVenda(self,novoPrecoV):
        
        self.__precoVenda = novoPrecoV
    
    def getQuantidade(self):
        
        print(self.__quantidade)
                
    
#Função para retornar todas as informações sobre o produto através de pesquisa
def getInfo(tipo,marca):
    
    with open('arquivos\estoque.json','r') as arquivo:
        
        conteudoArquivo = json.load(arquivo)
        
        if tipo in conteudoArquivo:
            if  conteudoArquivo[tipo]["marca"] == marca:
                print('Produto:',tipo)
                print('Marca:',conteudoArquivo[tipo]["marca"])
                print('Categoria:',conteudoArquivo[tipo]["categoria"])
                print('Preço de compra:',conteudoArquivo[tipo]["preco_de_compra"])
                print('Preço de venda:',conteudoArquivo[tipo]["preco_de_venda"])
                print('Quantidade em estoque:',conteudoArquivo[tipo]["quantidade"])
            else:
                print('Não existe este tipo de produto desta marca no sistema')
        else:
            print('O produto não consta no sistema')
    
#Função para alteração da categoria do produto através de pesquisa
def setCategoria(tipoProduto,marca,novaCategoria):
    
    with open('arquivos\estoque.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempCategoria:
        
        conteudoArquivo = json.load(arquivo)
        #Verifica se o tipo de produto informado consta no arquivo 
        if tipoProduto in conteudoArquivo:
            #Verifica a marca do produto
            if conteudoArquivo[tipoProduto]["marca"] == marca:
                conteudoArquivo[tipoProduto]["categoria"] = novaCategoria
            else:
                print('Não existe este tipo de produto desta marca no sistema')
                
            json.dump(conteudoArquivo,tempCategoria,ensure_ascii=False,indent=4)
        else:
            print('O produto não consta no sistema')
    
    shutil.move(tempCategoria.name,'arquivos\estoque.json')

#Função para a alteração do valor de compra através de pesquisa
def setPrecoCompra (tipoProduto,marca,novoPreco):
    
    with open('arquivos\estoque.json') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempPrecoCompra:
            
        conteudoArquivo = json.load(arquivo)
        
        if tipoProduto in conteudoArquivo:
            #Verificação da marca do produto
            if conteudoArquivo[tipoProduto]["marca"] == marca:
                conteudoArquivo[tipoProduto]["preco_de_compra"] = novoPreco
            else:
                 print('Não existe este tipo de produto desta marca no sistema')
        
            json.dump(conteudoArquivo,tempPrecoCompra,ensure_ascii=False,indent=4)
        else:
            print('O produto não consta no sistema')
    
    shutil.move(tempPrecoCompra.name,'arquivos\estoque.json')

#Função para alteração do valor de venda através de pesquisa
def setPrecoVenda (tipoProduto,marca,novoPreco):
    
    with open('arquivos\estoque.json') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempPrecoVenda:
        
        conteudoArquivo = json.load()
        
        if tipoProduto in conteudoArquivo:
            #Verificação da marca do produto
            if conteudoArquivo[tipoProduto]["marca"] == marca:
                conteudoArquivo[tipoProduto]["preco_de_venda"] = novoPreco
            else:
                print('Não existe este tipo de produto desta marca no sistema')
        else:
            print('O produto não consta no sistema')
        
        json.dump(conteudoArquivo,tempPrecoVenda,ensure_ascii=False,indent=4)
    
    shutil.move(tempPrecoVenda.name,'arquivos\estoque.json') 

    


    
        
        
        
    
        
        
    
    