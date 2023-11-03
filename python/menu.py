import json
import classPedido
from classPedido import Pedido

def menu():
    
    while True:
        
        print('*************************************************')
        print('1 - Funcionario')
        print('2 - Fornecedor')
        print('0 - Sair')
        escolha = input('Selecione a opção desejada:')
        print('*************************************************')
        
        if escolha == "1":
            
            inputUsuario = input('Usuario:')
            senhaUsuario = input('Senha:')
            
            with open('arquivos\\usuario.json','r') as usuarios:
                 
                infoUsuarios = json.load(usuarios)
                
                if inputUsuario in infoUsuarios:
                    if infoUsuarios[inputUsuario]["senha"] == senhaUsuario:
                        print('*************************************************')
                        print('Logado com sucesso...')
                        print('*************************************************')
                        print('Menu funcionário')
                        print('*************************************************')
                        print('1 - Verificar estoque')
                        print('2 - Realizar pedido')
                        print('3 - Finalizar pedido')
                        print('4 - Verificar pedidos')
                        print('5 - Cadastrar produto')
                        print('6 - Cadastrar fornecedor')
                        print('7 - Verificar movimentações')
                        print('0 - Sair')
                        escolhaUsuario = input('Selecione a opção desejada:')
                        print('*************************************************')
                        
                        
                        #if escolhaUsuario == "1":
                            
                            
                        
                        if escolhaUsuario == "2":
                            
                            inputNumero = input('Informe o número do pedido:')
                            inputTipo = input('Insira o tipo de pedido (entrada/saida):')
                            itens = []
                            
                            while True:
                                inputItem = input('Insira o item no pedido:')
                                itens.append(inputItem)
                                
                                print('*************************************************')
                                
                                print('0 - Parar inserção de itens no pedido')
                                print('1 - Adicionar novo item')
                                
                                continueItem = input('Informe sua escolha:')
                                
                                if continueItem == "0":
                                    break
                                
                                print('*************************************************')


                                
                            print('*************************************************')
                            
                            novoPedido = Pedido(inputNumero,inputTipo,itens)
                            
                            print('Pedido criado')
                            novoPedido.getInfo()
                        
                            
                        '''    
                        
                        elif escolhaUsuario == "3":
                            
                            
                        
                        elif escolhaUsuario == "4":
                            
                        
                        
                        elif escolhaUsuario == "5":
                            
                        
                        elif escolhaUsuario == "6":
                            
                        
                        elif escolhaUsuario == "7":
                            
                        
                        
                        elif escolhaUsuario == "0":
                        
                        
                        else:
                            print("Valor inválido")
                            
                        
                        
                    

                        
                        
                        
                    
                else:
                    print('************************** ***********************')
                    print('Usuário ou senha incorreta')
                    print('*************************************************')
                    
            
        elif escolha == '2':
        
            inputNomeForn = input('Nome:')
            senhaFornecedor = input('Senha:')
            
            with open('arquivos\\fornecedor.json','r') as fornecedores:
                
                conteudoFornecedores = json.load(fornecedores)
                
                if inputNomeForn in conteudoFornecedores:
                    if conteudoFornecedores[inputNomeForn]["senha"] == senhaFornecedor:
                        
                        print('**************************************************')
                        print('Logado com sucesso...')
                        
            
        elif escolha == '0':
            print('Encerrando...')
            return False
        '''
            
    
            