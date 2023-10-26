from datetime import date
import json
import tempfile
import shutil
import os

#Feito

class Pedido:
    
    def __init__(self,numeroPedido,itens=[]):
        
        self.__numeroPedido = numeroPedido
        self.__itensPedido = itens
        
    
    #Feito
    
    def realizarPedido(self):
        
        dadosPedido = {'itens':self.__itensPedido}
        
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
            
        #
        shutil.move(out.name,'arquivos\pedidos.json')
            
#Feito

def pesquisaPedido(numeroPedido):
    
    arquivoPedido = open('arquivos\pedidos.json','r')
    conteudoPedido = json.load(arquivoPedido)
    
    if numeroPedido in conteudoPedido:
            print(f'Pedido {numeroPedido} existe')
            
            print('Itens do pedido:',conteudoPedido[numeroPedido]["itens"])
            
    else:
            print(f'Pedido {numeroPedido} inexistente')
    
        

def excluiPedido(numeroPedido):
    
    arquivoPedido = open('arquivos\pedidos.json','r')
    conteudoPedido = json.load(arquivoPedido)
    
    if numeroPedido in conteudoPedido:
        
        print(f'Pedido {numeroPedido} excluido')
    
    else:
        print('Pedido inexistente')
        