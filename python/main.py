from classFornecedor import Fornecedor
from classProduto import Produto
from classPedido import Pedido
import classPedido
import classFornecedor as fornecedores


f1 = Fornecedor('a',123,'abc@gmail.com',['asd','dsads'])
f1.cadastrarFornecedor()

f2 = Fornecedor('b',456,'def@gmail.com',['oi','tchau'])
f2.cadastrarFornecedor()


fornecedores.getNome('b')

#fornecedores.setEmailFornecedor('b','12345@gmail.com')

fornecedores.getNome('b')

#fornecedores.getNome('c')

'''
p1 = Pedido('12874',['dsa','oi'])

p1.realizarPedido()

p2 = Pedido('678',[1,2])

p2.realizarPedido()

classPedido.pesquisaPedido("12874")

classPedido.excluiPedido("678")
'''