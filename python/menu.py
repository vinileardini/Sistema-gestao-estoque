import json
import tempfile
import shutil
import classPedido
from classPedido import Pedido
from classProduto import Produto
from classFornecedor import Fornecedor
import classFornecedor
import classProduto


def menu():
    
    while True:
        
        print('*************************************************')
        print('1 - Funcionario')
        print('2 - Fornecedor')
        print('0 - Sair')
        escolha = input('Selecione a opção desejada:')
        print('*************************************************')
        
        #Login usuario - OK
        if escolha == "1":
            
            inputUsuario = input('Usuario:')
            senhaUsuario = input('Senha:')
            
            while True:    
                with open('arquivos\\usuario.json','r') as usuarios:
                    
                    infoUsuarios = json.load(usuarios)
                    
                    if inputUsuario in infoUsuarios:
                        if infoUsuarios[inputUsuario]["senha"] == senhaUsuario:
                            print('*************************************************')
                            print('Menu funcionário')
                            classProduto.verificaQuantidadeEstoque()
                            print('*************************************************')
                            print('1 - Verificar estoque')
                            print('2 - Realizar pedido')
                            print('3 - Finalizar pedido')
                            print('4 - Verificar pedidos')
                            print('5 - Cadastrar produto')
                            print('6 - Cadastrar fornecedor')
                            print('7 - Verificar movimentações')
                            print('8 - Cadastrar funcionario')
                            print('0 - Sair')
                            escolhaUsuario = input('Selecione a opção desejada:')
                            print('*************************************************')
                            
                            # Verificar estoque - OK
                            if escolhaUsuario == "1":
                                
                                classProduto.verificaEstoque()
                                
                                
                            # Realizar pedido - OK
                            elif escolhaUsuario == "2":
                                
                                inputNumero = input('Informe o número do pedido:')
                                inputTipo = input('Insira o tipo de pedido (entrada/saida):')
                                inputNomeForn = input('Insira o nome do fornecedor:')
                                itens = []
                                
                                while True:
                                    inputItem = input('Insira o item no pedido:')
                                    itens.append(inputItem)
                                    inputQtItem = input('Insira a quantidade do item:')
                                    
                                    print('*************************************************')
                                    
                                    print('0 - Parar inserção de novo item no pedido')
                                    print('1 - Adicionar novo item')
                                    
                                    continueItem = input('Informe sua escolha:')
                                    
                                    if continueItem == "0":
                                        break
                                    
                                    elif continueItem != 0 and continueItem != 1:
                                        print('Opção inválida !!! Retornando ao menu')
                                        break
                                    
                                    
                                if inputTipo == "entrada":
                                    
                                    classPedido.pedidoEntrada(inputItem,inputQtItem)
                                    
                                elif inputTipo == "saida":
                                    
                                    classPedido.pedidoSaida(inputItem,inputQtItem)


                                print('*************************************************')
                                
                                novoPedido = Pedido(inputNumero,inputTipo,inputNomeForn,itens)
                                
                                with open('arquivos\pedidos.json','r') as arqPedidos:
                                    
                                    conteudoPedidos = json.load(arqPedidos)
                                    
                                    if inputNumero in conteudoPedidos:
                                    
                                        print('Pedido criado')
                                
                                        print('*************************************************')
                                
                                        novoPedido.getInfo()
                                    
                                    else:
                                        print('Não foi possível criar o pedido')
                                        
                                        print('*************************************************')
                            
                                
                            
                            # Finalizar pedido - OK
                            elif escolhaUsuario == "3":
                                
                                inputNumPedido = input('Insira o número do pedido a ser finalizado:')
                                
                                classPedido.encerrarPedido(inputNumPedido)
                                
                            # Verificar pedidos - lista todos - OK 
                            elif escolhaUsuario == "4":
                                
                                classPedido.listarPedidos()
                                
                            
                            #Cadastro de produto - OK
                            elif escolhaUsuario == "5":
                                
                                inputTipo = input('Insira o tipo de item:')
                                inputMarca = input('Insira a marca do produto:')
                                inputCategoria = input('Insira a categoria do produto:')
                                inputPrecoCompra = input('Insira o valor de compra do produto:')
                                inputPrecoVenda = input('Insira o valor de venda do produto:')
                                inputQuantidade = input('Insira a quantidade do produto:')
                                
                                try:
                                    novoProduto = Produto(inputTipo,inputMarca,inputCategoria,inputPrecoCompra,inputPrecoVenda,inputQuantidade)
                                    novoProduto.getInfo()
                                except:
                                    print('*************************************************')
                                    print('Não foi possível cadastrar o produto')
                                    print('Retornando ao menu')
                                
                            #Cadastro de fornecedor - OK
                            elif escolhaUsuario == "6":
                                
                                inputNomeForn = input('Insira o nome do fornecedor:')
                                inputTelefone = input('Insira o telefone do fornecedor:')
                                inputEmail = input('Insira o email do fornecedor:')
                                itensForn = []
                                
                                while True:
                                    
                                    novoItem = input('Insira o item fornecido:')
                                    itensForn.append(novoItem)
                                    
                                    print('*************************************************')
                                    
                                    print('0 - Parar inserção de novo item fornecido')
                                    print('1 - Adicionar novo item')
                                    
                                    escolhaCont = input('Escolha a opção desejada:')
                                    
                                    print('*************************************************')
                                    
                                    if escolhaCont == "0":
                                        print("Encerrando")
                                        break
                                    
                                    print('*************************************************')
                                try:
                                    Fornecedor(inputNomeForn,inputTelefone,inputEmail,itensForn)
                                except:
                                    print('Não foi possível cadastrar o fornecedor')
                                
                            #Verificação de movimentações - OK 
                            elif escolhaUsuario == "7":
                                
                                classPedido.verificarMovimentacao()
                            
                            #Cadastro de novo funcionario
                            elif escolhaUsuario == "8":
                                
                                cadastNome = input('Insira o nome do funcionario a ser cadastrado:')
                                
                                with tempfile.NamedTemporaryFile('w',delete=False) as tempFunc:
                                    
                                    if cadastNome not in infoUsuarios:
                                        
                                        while True:
                                            
                                            cadastSenha = input('Defina a senha para o usuário:')
                                            repeteSenha = input('Insira novamente a senha:')
                                            
                                            if cadastSenha == repeteSenha:
                                                dadosUser = {"senha":cadastSenha}
                                                infoUsuarios[cadastNome] = dadosUser
                                                json.dump(infoUsuarios,tempFunc,ensure_ascii=False,indent=4)
                                                print('Funcionario cadastrado')
                                                break
                                            
                                            else:
                                                print('As senhas informadas são diferentes')
                                    
                                    else:
                                        print('Funcionário já cadastrado')
                                            
                                shutil.move(tempFunc.name,'arquivos\\usuario.json')   
                                    
                                    
                                
                                
                                
                            #Encerra
                            elif escolhaUsuario == "0":
                                
                                print('Retornando a área de login ')
                                break
                            
                            else:
                                print("Valor inválido")            
                        
                    
                    else:
                        print('*************************************************')
                        print('Usuário ou senha incorreta')
                        break
                    
                    
                    
                    
        # Login fornecedor - OK
        elif escolha == '2':
            
            inputNomeForn = input('Nome:')
            senhaFornecedor = input('Senha:')
            
            with open('arquivos\\fornecedor.json','r') as fornecedores,\
                tempfile.NamedTemporaryFile('w',delete=False) as tempFornecedores:
                
                conteudoFornecedores = json.load(fornecedores)

                try:
                    if conteudoFornecedores[inputNomeForn]["senha"] == None:
                    
                        print("É o seu primeiro acesso")
                        novaSenha = input("Insira a nova senha:")
                        verificaSenha = input("Insira novamente a senha:")
                        
                        if novaSenha == verificaSenha:
                        
                            conteudoFornecedores[inputNomeForn]["senha"] = novaSenha
                    
                        else:
                            print('Fornecedor já cadastrado')
                
                        json.dump(conteudoFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                
                        shutil.move(tempFornecedores.name,'arquivos\\fornecedor.json')
                    
                    
                    elif conteudoFornecedores[inputNomeForn]["senha"] == senhaFornecedor:
                            print('*************************************************')            
                            print('Menu fornecedor')
                            print('**************************************************')
                            print('1 - Verificar informações')
                            print('2 - Alterar informações')
                            print('3 - Visualizar pedidos')
                            print('0 - Sair')
                            escolhaForn = input('Insira a opção desejada:')
                            print('*************************************************')

                            # Verificar as informações do fornecedor - OK
                            if escolhaForn == "1":

                                classFornecedor.getInfoFornecedor(inputNomeForn)
                                        
                            # Alterar informações do fornecedor - OK
                            elif escolhaForn == "2":
                                
                                while True:
                                    print('*************************************************')
                                    print('1 - Alterar telefone')
                                    print('2 - Alterar email')
                                    print('3 - Adicionar item oferecido')
                                    print('4 - Remover item oferecido')
                                    print('0 - Sair')
                                    
                                    escolhaAlteracao = input('Escolha a opção desejada:')
                                    
                                    print('*************************************************')
                            
                                    # Alteração telefone fornecedor - OK
                                    if escolhaAlteracao == "1":
                                        
                                        novoTel = input('Insira o novo telefone:')
                                        
                                        classFornecedor.setTelefoneFornecedor(inputNomeForn,novoTel)
                                    
                                    # Alteração email fornecedor - OK
                                    elif escolhaAlteracao == "2":
                                        
                                        novoEmail = input('Insira o novo email:')
                                        
                                        classFornecedor.setEmailFornecedor(inputNomeForn,novoEmail)
                                    
                                    # Adição item oferecido pelo fornecedor - OK
                                    elif escolhaAlteracao == "3":
                                        
                                        classFornecedor.setProdutosFornecedor(inputNomeForn)
                                    
                                    # Remoção item oferecido pelo fornecedor - OK
                                    elif escolhaAlteracao == "4":
                                        
                                        itemRemovido = input('Insira o item a ser removido:')
                                        classFornecedor.removeItem(inputNomeForn,itemRemovido)
                                        
                                    # Encerra - OK
                                    elif escolhaAlteracao == "0":
                                        
                                        print('Retornando a área do fornecedor')
                                        break
                                    
                                    else:
                                        print('Número de escolhido inválido')
                
                except:
                    print('Fornecedor não cadastrado ou senha incorreta')
            
                json.dump(conteudoFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                
            shutil.move(tempFornecedores.name,'arquivos\\fornecedor.json')
            
            
        elif escolha == '0':
            print('Encerrando...')
            return False

        
        else:
            print('Selecione uma opção válida')
        
            
    
            