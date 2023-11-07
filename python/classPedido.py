from datetime import *
import json
import tempfile
import shutil
import os

#Feito

class Pedido:
    
    def __init__(self,numeroPedido,tipo,fornecedor,itens=[]):
        
        self.__numeroPedido = numeroPedido
        self.__tipo = tipo
        self.__fornecedor = fornecedor
        self.__itensPedido = itens
        self.__status = 'aberto'
        
        data_e_hora = datetime.now()
        dadosPedido = {'data abertura': data_e_hora.strftime('%d/%m/%Y %H:%M:%S'),'tipo': self.getTipoPedido(),'status':self.getStatusPedido(),'itens':self.getItensPedido()}

        #Verificação se o fornecedor está cadastrado
        with open('arquivos\cadastroFornecedor.json','r') as arqFornecedor:
            
            conteudoArquivo = json.load(arqFornecedor)
            
            if self.getFornecedor() in conteudoArquivo:
                
                    dadosPedido = {'data abertura': data_e_hora.strftime('%d/%m/%Y %H:%M:%S'),'tipo': self.getTipoPedido(),'fornecedor':self.getFornecedor(),'status':self.getStatusPedido(),'itens':self.getItensPedido()}
        
            else:
                print('Fornecedor não cadastrado')
                
        with open('arquivos\pedidos.json','r') as saida, \
            open('arquivos\movimentacoes.json','r') as saidaMov,\
                tempfile.NamedTemporaryFile('w',delete=False) as out,\
                tempfile.NamedTemporaryFile('w',delete=False) as outMov:
                                        
                dados = json.load(saida)
                
                if not dados:
                    novoDado={}
                    novoDado[self.getNumeroPedido()] = dadosPedido
                    json.dump(novoDado,out,ensure_ascii=False,indent=4)
                    json.dump(novoDado,outMov,ensure_ascii=False,indent=4)
                    
                else:
                    dados[f'{self.getNumeroPedido()}'] = dadosPedido
                    json.dump(dados,out,ensure_ascii=False,indent=4,separators=(',',':'))
                    json.dump(dados,outMov,ensure_ascii=False,indent=4)
            
        
        shutil.move(out.name,'arquivos\pedidos.json')
        shutil.move(outMov.name,'arquivos\movimentacoes.json')
    
    
    def getNumeroPedido(self):
        
        return self.__numeroPedido
    
    def getTipoPedido(self):
        
        return self.__tipo
        
    def getItensPedido(self):
        
        return self.__itensPedido
        
    def getStatusPedido(self):
        
        return self.__status
    
    def getFornecedor(self):
        
        return self.__fornecedor

    
    def getInfo(self):
        
        print('Número do pedido:',self.getNumeroPedido())
        print('Tipo:',self.getTipoPedido())
        print('Fornecedor:',self.getFornecedor())
        print('Itens:',self.getItensPedido())
        print('Status:',self.getStatusPedido())
    
        
    def finalizaPedido(self):
        
        self.__status = "finalizado"
        
        with open('arquivos\pedidos.json','r') as saida,\
            open ('arquivos\movimentacoes.json','r') as saidaMov,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempPedido,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempMov:
                    
            conteudoPedidos = json.load(saida)
            conteudoMov = json.load(saidaMov)
            
            conteudoPedidos[self.__numeroPedido]["status"] = "finalizado"
            json.dump(conteudoPedidos,tempPedido,ensure_ascii=False,indent=4)
            
            if conteudoMov[self.__numeroPedido]["status"] == "aberto":
                
                conteudoMov[self.__numeroPedido]["status"] = "finalizado"
                
                data_e_hora = datetime.now()
                
                conteudoMov[self.__numeroPedido]["data fechamento"] = data_e_hora.strftime('%d/%m/%Y %H:%M:%S')
                
                json.dump(conteudoMov,tempMov,ensure_ascii=False,indent=4)
        
        shutil.move(tempPedido.name,'arquivos\pedidos.json')
        shutil.move(tempMov.name,'arquivos\movimentacoes.json')
        

#Pesquisas fora da classe

def pesquisaPedido(numeroPedido):

    arquivoPedido = open('arquivos\pedidos.json','r')
    conteudoPedido = json.load(arquivoPedido)

    if numeroPedido in conteudoPedido:
        print(f'Pedido {numeroPedido} existe')
        
        print('Itens do pedido:',conteudoPedido[numeroPedido]["itens"])
        
    else:
        print(f'Pedido {numeroPedido} inexistente')


def getStatus(numeroPedido):

    arquivoPedido = open('arquivos\pedidos.json','r')
    conteudoPedido = json.load(arquivoPedido)

    if numeroPedido in conteudoPedido:
    
        print('O status do pedido é:',conteudoPedido[numeroPedido]["status"])

    else:
        print('Pedido inexistente')

# Pronto
def encerrarPedido(numeroPedido):

    with open('arquivos\pedidos.json','r') as arquivoPedido,\
        open('arquivos\movimentacoes.json','r') as arquivoMov,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempPedido,\
            tempfile.NamedTemporaryFile('w',delete=False) as tempMov:
        
        
        conteudoPedido = json.load(arquivoPedido)
        conteudoMov = json.load(arquivoMov)
        #verifica existencia do pedido
        if numeroPedido in conteudoPedido:
            #verifica status do pedido
            if conteudoPedido[numeroPedido]["status"] != "finalizado":
                
                conteudoPedido[numeroPedido]["status"] = "finalizado"
                conteudoMov[numeroPedido]["status"] = "finalizado"
                json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
                json.dump(conteudoMov,tempMov,ensure_ascii=False,indent=4)
                
                print('Pedido finalizado')
            
            else:
                print('Pedido já finalizado')
                
        else:
            print('Pedido inexistente')
                
    shutil.move(tempPedido.name,'arquivos\pedidos.json')
    
        
                            
                            

# função para excluir um pedido (pronto)
def excluiPedido(numeroPedido):

    with open('arquivos\pedidos.json','r') as arquivoPedido,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempPedido:
        
        conteudoPedido = json.load(arquivoPedido)

        if conteudoPedido.HasKey(numeroPedido):
            #Exclui o pedido informado do dicionario
            conteudoPedido.pop(numeroPedido)
            print(f'Pedido {numeroPedido} excluido')
            json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)

        else:
            print('Pedido inexistente')

    shutil.move(tempPedido.name,'arquivos\pedidos.json')

def listarPedidos():
    
    with open('arquivos\pedidos.json','r') as arqPedidos:
        
        pedidos = json.load(arqPedidos)
        
        for chave in pedidos.items():
            print(chave)
        

def verificarMovimentacao():
    
    with open('arquivos\movimentacoes.json','r') as arqMov:
        
        conteudoArquivo = json.load(arqMov)
        
        print(conteudoArquivo.items())
        

def pedidoEntrada(tipoProduto,quantidade):
    
    with open('arquivos\estoque.json','r') as arqEstoque,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempEstoque:
        
        conteudoArquivo = json.load(arqEstoque)
        
        quantidadeEstoque = conteudoArquivo[tipoProduto]["quantidade"]
        
        conteudoArquivo[tipoProduto]["quantidade"] = int(quantidadeEstoque) + int(quantidade)
        
        json.dump(conteudoArquivo,tempEstoque,ensure_ascii=False,indent=4)
    
    shutil.move(tempEstoque.name,'arquivos\estoque.json')
        

def pedidoSaida(tipoProduto,quantidade):   
    
    with open('arquivos\estoque.json', 'r') as arqEstoque,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempEstoque:
            
        conteudoArquivo = json.load(arqEstoque)
        
        quantidadeEstoque = conteudoArquivo[tipoProduto]["quantidade"]
        
        conteudoArquivo[tipoProduto]["quantidade"] = int(quantidadeEstoque) - int(quantidade)
        
        json.dump(conteudoArquivo,tempEstoque,ensure_ascii=False,indent=4)
    
    shutil.move(tempEstoque.name,'arquivos\estoque.json')