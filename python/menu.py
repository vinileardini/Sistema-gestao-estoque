import json

def menu():
    
    while True:
        
        print('*************************************************')
        print('1 - Funcionario')
        print('2 - Fornecedor')
        print('0 - Sair')
        escolha = input('Selecione a opção desejada:')
        print('*************************************************')
        
        if escolha == '1':
            
            inputUsuario = input('Usuario:')
            senhaUsuario = input('Senha:')
            
            with open('arquivos\usuario.json','r') as usuarios:
                 
                infoUsuarios = json.load(usuarios)
                
                if inputUsuario in infoUsuarios:
                    if infoUsuarios[inputUsuario]["senha"] == senhaUsuario:
                        print('*************************************************')
                        print('Logado com sucesso...')
                    else:
                        print('Usuario ou senha incorreta')
                    
                else:
                    print('*************************************************')
                    print()
                    
            
        elif escolha == '2':
        
            inputNomeForn = input('Nome:')
            senhaFornecedor = input('Senha:')
            
        elif escolha == '0':
            print('Encerrando...')
            return False
            
            