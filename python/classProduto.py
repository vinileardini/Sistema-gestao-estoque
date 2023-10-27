
import tempfile
import shutil
import json


class Produto:
    
    def __init__(self,nome,categoria,precoVenda,quantidadeProduto):
        
        self.nomeProduto = nome
        self.categoriaProduto = categoria
        self.precoVenda = precoVenda
        self.quantidade = quantidadeProduto
        
    #Feito
    def adicionarProduto(self):
        
        with open('arquivos\estoque.json','r') as arquivo,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempProduto:
                
            conteudoArquivo = json.load(arquivo)
            
            if self.nomeProduto not in conteudoArquivo:
                
                dadosProduto = {'categoria':self.categoriaProduto,'preco':self.precoVenda,'quantidade':self.quantidade}
                
                conteudoArquivo[self.nomeProduto] = dadosProduto
                json.dump(conteudoArquivo,tempProduto,ensure_ascii=False,indent=4)
            
            else:
                
                conteudoArquivo[self.nomeProduto]["quantidade"] += self.quantidade
                json.dump(conteudoArquivo,tempProduto,ensure_ascii=False,indent=4)
                
        shutil.move(tempProduto.name,'arquivos\estoque.json')
                
    
#Feito
def getInfo(nome):
    
    with open('arquivos\estoque.json','r') as arquivo:
        
        conteudoArquivo = json.load(arquivo)
        
        if nome in conteudoArquivo:
            print('Produto:',conteudoArquivo[nome])
            print('Categoria:',conteudoArquivo[nome]["categoria"])
            print('Preço de venda:',conteudoArquivo[nome]["preco"])
            print('Quantidade em estoque:',conteudoArquivo[nome]["quantidade"])
    

def setCategoria(nomeProduto,novaCategoria):
    
    with open('arquivos\estoque.json','r') as arquivo,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempCategoria:
        
        conteudoArquivo = json.load(arquivo)
        
        if nomeProduto in conteudoArquivo:
            
            conteudoArquivo[nomeProduto]["categoria"] = novaCategoria
            json.dump(conteudoArquivo,tempCategoria,ensure_ascii=False,indent=4)
        
        else:
            print('Não existe produto com esse nome')
    
    shutil.move(tempCategoria.name,'arquivos\estoque.json')

'''
def setPreco (nome,novoPreco):
    
'''


    


    
        
        
        
    
        
        
    
    