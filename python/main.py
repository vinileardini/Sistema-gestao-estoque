from classFornecedor import Fornecedor
from classProduto import Produto
from classPedido import Pedido
import classPedido
import classFornecedor as fornecedores
import classProduto as produtos

'''Teste Fornecedor
f1 = Fornecedor('a',123,'abc@gmail.com',['asd','dsads'])
f1.cadastrarFornecedor()

f2 = Fornecedor('b',456,'def@gmail.com',['oi','tchau'])
f2.cadastrarFornecedor()

fornecedores.getInfo('b')

fornecedores.setTelefoneFornecedor('a',786)

fornecedores.setEmailFornecedor('b','12345@gmail.com')

fornecedores.getInfo('b')

fornecedores.getInfo('c')
'''

'''Teste Pedido
p1 = Pedido('12874',['dsa','oi'])

p1.realizarPedido()

p2 = Pedido('678',[1,2])

p2.realizarPedido()

classPedido.pesquisaPedido("12874")

classPedido.excluiPedido("678")
'''

'''Teste Produto
'''

prod1 = Produto('mouse','periferico',130.00,5)
prod1.adicionarProduto()

prod2 = Produto('camiseta','vestuario',70.00,32)
prod2.adicionarProduto()

produtos.getInfo('mouse')

produtos.setCategoria('mouse','eletronico')
produtos.setCategoria('teclado','eletronico')