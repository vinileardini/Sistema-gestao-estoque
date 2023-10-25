import os
import pathlib


class Produto:
    
    def __init__(self,nome,categoria,precoVenda,quantidadeProduto):
        
        self.nomeProduto = nome
        self.categoriaProduto = categoria
        self.precoVenda = precoVenda
        self.__quantidade = quantidadeProduto
    
    
    
    def setNomeProduto (self,nomeAlterado):
        
        self.nomeProduto = nomeAlterado
    
    def getNome (self):
        
        return self.nomeProduto
    
    def setCategoria(self,alteraCategoria):
        
        self.categoriaProduto = alteraCategoria
    
    def getCategoria (self):
        
        return self.categoriaProduto

    def setPreco (self,novoPreco):
        
        self.precoVenda = novoPreco
    
    def getPreco (self):
        
        return self.precoVenda
    
    def getQuantidade(self):
    
        return self.__quantidade
    
    
        
        
        
    
        
        
    
    