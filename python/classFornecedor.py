from typing import Any


class Fornecedor:
    
    def __init__(self,nome,telefone,email,produtos=[]):
        
        self.nomeFornecedor = nome
        self.telefoneFornecedor = telefone
        self.email = email
        self.produtos = produtos
        
    
    def getNome(self):
        
        return self.nomeFornecedor
    
    def getEmailFornecedor(self):
        
        return self.email
    
    def getTelefoneFornecedor(self):
        
        return self.telefoneFornecedor
    
    def getProdutosFornecedor(self):
        
        for produto in self.produtos:
            print(self.produtos[produto])
    
    def setNome(self,alteraNome):
        
        self.nomeFornecedor = alteraNome
    
    def setEmailFornecedor(self,novoEmail):
        
        self.email = novoEmail
    
    def setTelefoneFornecedor(self,novoTelefone):
        
        self.telefoneFornecedor = novoTelefone

    
        
        