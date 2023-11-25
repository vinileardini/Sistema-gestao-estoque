from datetime import *
import json
import tempfile
import shutil
import os


#Feito

class Pedido:
    
    def __init__(self,numeroPedido,tipo,fornecedor,itens=[],qtItens=[]):
        
        self.__numeroPedido = numeroPedido
        self.__tipo = tipo
        self.__fornecedor = fornecedor
        self.__itensPedido = itens
        self.__status = 'aberto'
        self.__qtItens = qtItens
        self.pedidoRealizado = True
        
        data_e_hora = datetime.now()
        dadosPedido = {'data abertura': data_e_hora.strftime('%d/%m/%Y %H:%M:%S'),'tipo': self.getTipoPedido(),'status':self.getStatusPedido(),'itens':self.getItensPedido(),'quantidade':self.getQtItensPedido()}

        #Verificação se o fornecedor está cadastrado - OK
        with open('arquivos\cadastroFornecedor.json','r') as arqFornecedor:
            
            conteudoArquivo = json.load(arqFornecedor)
            
            if self.getFornecedor() in conteudoArquivo:
                
                itensNaoFornecidos = 0
                
                for item in itens:
                    
                    if item in conteudoArquivo[self.getFornecedor()]["produtos"]: 
                        pass
                                      
                    else:
                        itensNaoFornecidos += 1
                    
                if itensNaoFornecidos == 0:
                    dadosPedido = {'data abertura': data_e_hora.strftime('%d/%m/%Y %H:%M:%S'),'tipo': self.getTipoPedido(),'fornecedor':self.getFornecedor(),'status':self.getStatusPedido(),'itens':self.getItensPedido(),'qtItens':self.getQtItensPedido()}
                        
                    with open('arquivos\pedidos.json','r') as saida,\
                        open('arquivos\movimentacoes.json','r') as saidaMov,\
                            tempfile.NamedTemporaryFile('w',delete=False) as out,\
                            tempfile.NamedTemporaryFile('w',delete=False) as outMov:
                                                    
                        dados = json.load(saida)
                            
                        if self.getNumeroPedido() not in dados:
                                    
                                    
                            if not dados:
                                novoDado={}
                                novoDado[self.getNumeroPedido()] = dadosPedido
                                json.dump(novoDado,out,ensure_ascii=False,indent=4)
                                json.dump(novoDado,outMov,ensure_ascii=False,indent=4)
                            
                            else:
                                dados[f'{self.getNumeroPedido()}'] = dadosPedido
                                json.dump(dados,out,ensure_ascii=False,indent=4,separators=(',',':'))
                                json.dump(dados,outMov,ensure_ascii=False,indent=4)
                                
                                

                            print('*************************************************')
                            print('Pedido criado')
                                
                            self.getInfo()
                                    
                        else:
                                print('Já existe um pedido com este número')  
                                
                                self.pedidoRealizado = False  
                        
                    if self.getPedidoRealizado() == True:
                            
                        shutil.move(out.name,'arquivos\pedidos.json')
                        shutil.move(outMov.name,'arquivos\movimentacoes.json')
                        
                    else:
                        pass
                else:
                    print('*************************************************')
                    print('Pedido não realizado')
                    print('Fornecedor não fornece item no pedido')
                               
            else:
                print('Fornecedor não cadastrado')
    
    
    def getPedidoRealizado(self):
        
        return self.pedidoRealizado
    
    def getNumeroPedido(self):
        
        return self.__numeroPedido
    
    def getTipoPedido(self):
        
        return self.__tipo
        
    def getItensPedido(self):
        
        return self.__itensPedido
    
    def getQtItensPedido(self):
        
        return self.__qtItens
        
    def getStatusPedido(self):
        
        return self.__status
    
    def getFornecedor(self):
        
        return self.__fornecedor
    
    def getQtItens(self):
        
        return self.__qtItens

    
    def getInfo(self):
        
        print('*************************************************')
        print('Número do pedido:',self.getNumeroPedido())
        print('Tipo:',self.getTipoPedido())
        print('Fornecedor:',self.getFornecedor())
        print('Itens:',self.getItensPedido())
        print('Quantidade de cada item:',self.getQtItens())
        print('Status:',self.getStatusPedido())
    

    #Pesquisas 

    # função para pesquisar a existência de um pedido
    def pesquisaPedido(numeroPedido):

        arquivoPedido = open('arquivos\pedidos.json','r')
        conteudoPedido = json.load(arquivoPedido)

        if numeroPedido in conteudoPedido:
            print(f'Pedido {numeroPedido} existe')
            
            print('Itens do pedido:',conteudoPedido[numeroPedido]["itens"])
            
        else:
            print(f'Pedido {numeroPedido} inexistente')

    # função para buscar o status do pedido (aberto/finalizado)
    def getStatus(numeroPedido):

        arquivoPedido = open('arquivos\pedidos.json','r')
        conteudoPedido = json.load(arquivoPedido)

        if numeroPedido in conteudoPedido:
        
            print('O status do pedido é:',conteudoPedido[numeroPedido]["status"])

        else:
            print('Pedido inexistente')

    # função para o encerramento de um pedido
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
                if conteudoPedido[numeroPedido]["status"] == "aberto":
                    
                    del(conteudoPedido[numeroPedido])
                    conteudoMov[numeroPedido]["status"] = "finalizado"
                    data_e_hora = datetime.now()
                    conteudoMov[numeroPedido]["data fechamento"] = data_e_hora.strftime('%d/%m/%Y %H:%M:%S')
                    json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
                    json.dump(conteudoMov,tempMov,ensure_ascii=False,indent=4)
                    
                    print('Pedido finalizado')
                
                else:
                    print('Pedido já finalizado')
                    json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
            
            else:
                print('Pedido inexistente')
                json.dump(conteudoPedido,tempPedido,ensure_ascii=False,indent=4)
                json.dump(conteudoMov,tempMov,ensure_ascii=False,indent=4)
            
        shutil.move(tempPedido.name,'arquivos\pedidos.json')
        shutil.move(tempMov.name,'arquivos\movimentacoes.json')
                    
           
            
                                
                                

    # função para excluir um pedido
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
        
    # função para listar os pedidos 
    def listarPedidos():
        
        with open('arquivos\pedidos.json','r') as arqPedidos:
            
            pedidos = json.load(arqPedidos)
            
            if len(pedidos) > 0:
            
                for chave in pedidos.keys():
                    
                    print('*************************************************')
                    print('Número do pedido:',chave)
                    print('Data abertura:',pedidos[chave]["data abertura"])
                    print('Tipo:',pedidos[chave]["tipo"])
                    print('Fornecedor:',pedidos[chave]["fornecedor"])
                    print('Itens:',pedidos[chave]["itens"])
                    print('Quantidade:',pedidos[chave]["qtItens"])
            
            else:
                print('Não existe pedidos em aberto')
            
            
    # função para verificar a movimentação 
    def verificarMovimentacao():
        try:
            with open('arquivos\movimentacoes.json','r') as arqMov:
                
                conteudoArquivo = json.load(arqMov)
                
                chaves = conteudoArquivo.keys()
                
                for chave in chaves:
                    
                    print('*************************************************')
                    print('Numero pedido:',chave)
                    print('Data abertura:',conteudoArquivo[chave]["data abertura"])
                    if "data fechamento" in conteudoArquivo[chave]:
                        print('Data de fechamento:',conteudoArquivo[chave]["data fechamento"])
                    print('Tipo movimentacao:',conteudoArquivo[chave]["tipo"])
                    print('Fornecedor:',conteudoArquivo[chave]["fornecedor"])
                    print('Itens:',conteudoArquivo[chave]["itens"])
        except:
            print('Não foi possivel verificar as movimentações')
                
            
            
            
    # função para realizar a adição de itens no estoque no caso do tipo do pedido for entrada
    def pedidoEntrada(tipoProduto,quantidade):
        try:
            with open('arquivos\estoque.json','r') as arqEstoque,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempEstoque:
                
                conteudoArquivo = json.load(arqEstoque)
                
                quantidadeEstoque = conteudoArquivo[tipoProduto]["quantidade"]
                
                conteudoArquivo[tipoProduto]["quantidade"] = int(quantidadeEstoque) + int(quantidade)
                
                json.dump(conteudoArquivo,tempEstoque,ensure_ascii=False,indent=4)
            
            shutil.move(tempEstoque.name,'arquivos\estoque.json')
        except:
            print("Produto não cadastrado")
            
    # função para retirar itens no estoque caso o tipo de pedido seja saída
    def pedidoSaida(tipoProduto,quantidade):   

        try:    
            with open('arquivos\estoque.json', 'r') as arqEstoque,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempEstoque:
                    
                conteudoArquivo = json.load(arqEstoque)
                
                quantidadeEstoque = conteudoArquivo[tipoProduto]["quantidade"]
                
                if int(quantidade) <= int(quantidadeEstoque):
                
                    conteudoArquivo[tipoProduto]["quantidade"] = int(quantidadeEstoque) - int(quantidade)
                
                    json.dump(conteudoArquivo,tempEstoque,ensure_ascii=False,indent=4)
                
                else:
                    print('Não foi possível realizar o pedido devido ao número de produtos no estoque')
                    
                    json.dump(conteudoArquivo,tempEstoque,ensure_ascii=False,indent=4)
                    
            shutil.move(tempEstoque.name,'arquivos\estoque.json')
            
           
        except:
            print("Produto não cadastrado")
            
    # função para verificar a quantidade de itens no estoque para que seja possível realizar pedido de saída
    def verificaQtEstoque(tipoProduto,tipoPedido,quantidade):
        
        try:
            with open('arquivos\estoque.json') as arqEstoque:
                
                conteudoArquivo = json.load(arqEstoque)
                
                quantidadeEstoque = conteudoArquivo[tipoProduto]["quantidade"]
                if tipoPedido == 'saida':
                    if int(quantidade) <= quantidadeEstoque:
                        
                        return True
                    
                    else:
                        print('Não existe essa quantidade deste produto em estoque neste momento')
                        return False
                elif tipoPedido ==  'entrada':
                    return True
                    pass
                
        except:
            print('Produto não cadastrado')