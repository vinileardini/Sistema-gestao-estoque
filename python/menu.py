import json
import tempfile
import shutil
from classPedido import Pedido
from classProduto import Produto
from classFornecedor import Fornecedor
from classFuncionario import Funcionario



def menu():
    
    while True:
        #Área de login
        print('*************************************************')
        print('1 - Funcionario')
        print('2 - Fornecedor')
        print('0 - Sair')
        escolha = input('Selecione a opção desejada:')
        print('*************************************************')
        
        #Login usuario 
        if escolha == "1":
            
            inputUsuario = input('Usuario:')
            senhaUsuario = input('Senha:')
            
        
            with open('arquivos\\usuario.json','r') as usuarios:
                    
                    infoUsuarios = json.load(usuarios)
                    
             
                    #Menu no modo funcionário
                    if inputUsuario in infoUsuarios:
                        if infoUsuarios[inputUsuario]["senha"] == senhaUsuario:
                            
                            while True:
                                print('*************************************************')
                                print('Menu funcionário')
                                Produto.verificaQuantidadeEstoque()
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
                                
                                # Verificar estoque
                                if escolhaUsuario == "1":
                                    
                                    Produto.verificaEstoque()
                                    
                                    
                                # Realizar pedido 
                                elif escolhaUsuario == "2":
                                    
                                    inputNumero = input('Informe o número do pedido:')
                                    inputTipo = input('Insira o tipo de pedido (entrada/saida):')
                                    inputNomeForn = input('Insira o nome do fornecedor:')
                                    itens = []
                                    qtItens = []
                                    
                                    #Verificação para a inserção de + um item no pedido
                                    while True:
                                        inputItem = input('Insira o item no pedido:')
                                        inputQtItem = input('Insira a quantidade do item:')
                                        
                                        if Pedido.verificaQtEstoque(inputItem,inputTipo,inputQtItem) == True:
                                            itens.append(inputItem)
                                            qtItens.append(inputQtItem)
                                        else:
                                            print('Item não adicionado ao pedido')
                                        
                                        print('*************************************************')
                                        
                                        print('0 - Parar inserção de novo item no pedido')
                                        print('1 - Adicionar novo item')
                                        
                                        continueItem = input('Informe sua escolha:')
                                        
                                        if continueItem == "0":
                                            break
                                        
                                        elif continueItem != '0' and continueItem != '1':
                                            print('Opção inválida !!! Retornando ao menu')
                                            break
                                    
                                    
                                        print('*************************************************')
                                    
                                    if len(itens) > 0:  
                                        novoPedido = Pedido(inputNumero,inputTipo,inputNomeForn,itens,qtItens)
                                    else:
                                        print('Pedido não realizado devido a não inserção de itens')
                                    
                                    try:
                                        if novoPedido.getPedidoRealizado() == True:
                                    
                                            if inputTipo == "entrada":
                                            
                                                Pedido.pedidoEntrada(inputItem,inputQtItem)
                                            
                                            elif inputTipo == "saida":
                                            
                                                Pedido.pedidoSaida(inputItem,inputQtItem)
                                            else:
                                                pass
                                    except:
                                        print('Pedido não realizado')
                                    
                                
                                    

                                
                                
                                # Finalizar pedido 
                                elif escolhaUsuario == "3":
                                    
                                    inputNumPedido = input('Insira o número do pedido a ser finalizado:')
                                    
                                    Pedido.encerrarPedido(inputNumPedido)
                                    
                                # Verificar pedidos - lista todos
                                elif escolhaUsuario == "4":
                                    
                                    Pedido.listarPedidos()
                                    
                                
                                #Cadastro de produto 
                                elif escolhaUsuario == "5":
                                    
                                    inputTipo = input('Insira o tipo de item:')
                                    inputMarca = input('Insira a marca do produto:')
                                    inputCategoria = input('Insira a categoria do produto:')
                                    inputPrecoCompra = input('Insira o valor de compra do produto:')
                                    inputPrecoVenda = input('Insira o valor de venda do produto:')
                                    inputQuantidade = input('Insira a quantidade do produto:')
                                    
                                    try:
                                        novoProduto = Produto(inputTipo,inputMarca,inputCategoria,inputPrecoCompra,inputPrecoVenda,inputQuantidade)
                                        print('*************************************************')
                                        print('Produto cadastrado')
                                        print('*************************************************')
                                        novoProduto.getInfo()
                                        
                                    except:
                                        print('*************************************************')
                                        print('Não foi possível cadastrar o produto')
                                        print('Retornando ao menu')
                                    
                                #Cadastro de fornecedor 
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
                                            print("Encerrando a inserção de itens")
                                            break
                                        
                                        print('*************************************************')
                                    try:
                                        Fornecedor(inputNomeForn,inputTelefone,inputEmail,itensForn)
                                        print('Fornecedor cadastrado')
                                    except:
                                        print('Não foi possível cadastrar o fornecedor')
                                    
                                #Verificação de movimentações 
                                elif escolhaUsuario == "7":
                                    
                                    Pedido.verificarMovimentacao()
                                
                                #Cadastro de novo funcionario
                                elif escolhaUsuario == "8":
                                    
                                    cadastNome = input('Insira o nome do funcionario a ser cadastrado:')
                                    registro = input('Insira o número de registro do funcionário:')
                                    
                                    try:
                                        Funcionario(cadastNome,registro)
                                    except:
                                        print('Não foi possível cadastrar o novo funcionário')    
                                    
                                    
                                    
                                    
                                    
                                #Encerra
                                elif escolhaUsuario == "0":
                                    
                                    print('Retornando a área de login ')
                                    break
                                
                                else:
                                    print("Valor inválido")         
                            
                        
                        else:
                            print('*************************************************')
                            print('Usuário ou senha incorreta')
                    else:
                        print('*************************************************')
                        print('Funcionário não cadastrado')
                        
                        
                        
                    
        # Login fornecedor 
        elif escolha == '2':
            
            inputNomeForn = input('Nome:')
            senhaFornecedor = input('Senha:')
            
            while True:
                    try:
                        
                        with open('arquivos\\fornecedor.json','r') as fornecedores,\
                        tempfile.NamedTemporaryFile('w',delete=False) as tempFornecedores:
                    
                            conteudoFornecedores = json.load(fornecedores)
                        
                            if conteudoFornecedores[inputNomeForn]["senha"] == None:
                            
                                print("É o seu primeiro acesso")
                                novaSenha = input("Insira a nova senha:")
                                verificaSenha = input("Insira novamente a senha:")
                                
                                if novaSenha == verificaSenha:
                                
                                    conteudoFornecedores[inputNomeForn]["senha"] = novaSenha
                                    json.dump(conteudoFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                            
                                else:
                                    print('Fornecedor já cadastrado')
                                    json.dump(conteudoFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                            else:
                                json.dump(conteudoFornecedores,tempFornecedores,ensure_ascii=False,indent=4)
                    
                        shutil.move(tempFornecedores.name,'arquivos\\fornecedor.json')
                        
                        
                        if conteudoFornecedores[inputNomeForn]["senha"] == senhaFornecedor:
                                print('*************************************************')            
                                print('Menu fornecedor')
                                print('**************************************************')
                                print('1 - Verificar informações')
                                print('2 - Alterar informações')
                                print('3 - Visualizar pedidos')
                                print('0 - Sair')
                                escolhaForn = input('Insira a opção desejada:')
                                print('*************************************************')

                                # Verificar as informações do fornecedor 
                                if escolhaForn == "1":

                                    Fornecedor.getInfoFornecedor(inputNomeForn)
                                            
                                # Alterar informações do fornecedor 
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
                                
                                        # Alteração telefone fornecedor 
                                        if escolhaAlteracao == "1":
                                            
                                            novoTel = input('Insira o novo telefone:')
                                            
                                            Fornecedor.setTelefoneFornecedor(inputNomeForn,novoTel)
                                        
                                        # Alteração email fornecedor 
                                        elif escolhaAlteracao == "2":
                                            
                                            novoEmail = input('Insira o novo email:')
                                            
                                            Fornecedor.setEmailFornecedor(inputNomeForn,novoEmail)
                                        
                                        # Adição item oferecido pelo fornecedor 
                                        elif escolhaAlteracao == "3":
                                            
                                            Fornecedor.setProdutosFornecedor(inputNomeForn)
                                        
                                        # Remoção item oferecido pelo fornecedor 
                                        elif escolhaAlteracao == "4":
                                            
                                            itemRemovido = input('Insira o item a ser removido:')
                                            Fornecedor.removeItem(inputNomeForn,itemRemovido)
                                            
                                        # Encerra 
                                        elif escolhaAlteracao == "0":
                                            
                                            print('Retornando a área do fornecedor')
                                            break
                                        
                                        else:
                                            print('Número escolhido inválido')
                                            
                                #Lista os pedidos vinculados ao fornecedor
                                elif escolhaForn == "3":
                                    
                                    Fornecedor.listaPedidosForn(inputNomeForn)
                                    
                                elif escolhaForn == "0":
                                    print('Retornando a área de login')
                                    break
                                    
                                else:
                                    print("Número escolhido inválido")
                                    
                    
                        else:
                            print('*************************************************')
                            print('Usuário ou senha incorreta')
                            break
                    except:
                        print('*************************************************')
                        print('Fornecedor não cadastrado')
                        break
                   
                    
            
            
        elif escolha == '0':
            print('Encerrando...')
            return False

        
        else:
            print('Selecione uma opção válida')
        
            
    
            