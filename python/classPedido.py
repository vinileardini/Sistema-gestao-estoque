from datetime import *
import json
import tempfile
import shutil
import os

#Feito

class Pedido:
    
    def __init__(self,numeroPedido,tipo,itens=[]):
        
        self.__numeroPedido = numeroPedido
        self.__tipo = tipo
        self.__itensPedido = itens
        self.__status = 'aberto'
        
    
    #Feito
    
    def realizarPedido(self):
        
        data_e_hora = datetime.now()
        dadosPedido = {'data abertura': data_e_hora.strftime('%d/%m/%Y %H:%M:%S'),'tipo': self.__tipo,'status':self.__status,'itens':self.__itensPedido,}
        
        with open('arquivos\pedidos.json','r') as saida, \
                tempfile.NamedTemporaryFile('w',delete=False) as out:
                    
                dados = json.load(saida)
                
                if not dados:
                    novoDado={}
                    novoDado[self.__numeroPedido] = dadosPedido
                    json.dump(novoDado,out,ensure_ascii=False,indent=4)
                    
                else:
                    dados[f'{self.__numeroPedido}'] = dadosPedido
                    json.dump(dados,out,ensure_ascii=False,indent=4,separators=(',',':'))
            
        
        shutil.move(out.name,'arquivos\pedidos.json')
        
        
    def getNumeroPedido(self):
        
        print(self.__numeroPedido)
    
    def getItensPedido(self):
        
        print(self.__itensPedido)
    
    def setItensPedido(self,novosItens):
        
        self.__itensPedido = novosItens
            
#Feito

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

#Pronto
def alteraStatus(numeroPedido,novoStatus):
    
    with open('arquivos\pedidos.json','r') as arquivoPedido,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempPedido:
    
        conteudoPedido = json.load(arquivoPedido)
    
        if numeroPedido in conteudoPedido:
        
            conteudoPedido[numeroPedido]["status"] = novoStatus
            json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
    
        else:
            print('Pedido inexistente')
    
    shutil.move(tempPedido,'arquivos\pedidos.json')
    
# Pronto
def finalizaPedido(numeroPedido):
    
    with open('arquivos\pedidos.json','r') as arquivoPedido,\
        tempfile.NamedTemporaryFile('w',delete=False) as tempPedido:
            
        conteudoPedido = json.load(arquivoPedido)
        #verifica existencia do pedido
        if numeroPedido in conteudoPedido:
            #verifica status do pedido
            if conteudoPedido[numeroPedido]["status"] != "finalizado":
                conteudoPedido[numeroPedido]["status"] = "finalizado"
                json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
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
    
        if numeroPedido in conteudoPedido:
            #Exclui o pedido informado do dicionario
            conteudoPedido.pop(numeroPedido)
            print(f'Pedido {numeroPedido} excluido')
            json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
    
        else:
            print('Pedido inexistente')
    
    shutil.move(tempPedido.name,'arquivos\pedidos.json')