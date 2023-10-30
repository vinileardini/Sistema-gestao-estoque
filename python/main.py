from classFornecedor import Fornecedor
from classProduto import Produto
from classPedido import Pedido
import classPedido
import classFornecedor as fornecedores
import classProduto as produtos

'''Teste Fornecedor
f1 = Fornecedor('a',123,'abc@gmail.com',['asd','dsads'])
f1.cadastrarFornecedor()
f1.getNome()
f1.getProdutos()
f1.getTelefone()
f1.getEmail()


f2 = Fornecedor('b',456,'def@gmail.com',['oi','tchau'])
f2.cadastrarFornecedor()

fornecedores.getInfo('b')

fornecedores.setTelefoneFornecedor('a',786)

fornecedores.setEmailFornecedor('b','12345@gmail.com')

fornecedores.getInfo('c')
'''

#Teste Pedido
p1 = Pedido('12874','entrada',['dsa','oi'])

p1.realizarPedido()

p2 = Pedido('678','entrada',[1,2])

p2.realizarPedido()

classPedido.pesquisaPedido("12874")

classPedido.finalizaPedido("678")

#classPedido.excluiPedido("678")


'''Teste Produto


prod1 = Produto('mouse','logitech','perifericos',80.00,99.99,20)
prod1.adicionarProduto(10)

prod2 = Produto("camiseta","polo","vestuario",70.00,150.00,32)
prod2.adicionarProduto(2)

produtos.getInfo('mouse','logitech')

produtos.setCategoria('mouse','logitech','periferico')
produtos.setCategoria('mouse','razer','eletronico')
'''