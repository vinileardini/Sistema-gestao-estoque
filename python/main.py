from classFornecedor import Fornecedor
from classProduto import Produto
from classPedido import Pedido
import classPedido


f1 = Fornecedor('a',123,'abc@gmail.com',['asd','dsads'])

arquivoFornecedor = open('arquivos\fornecedor.json','w')

p1 = Pedido('12874',['dsa','oi'])

p1.realizarPedido()

p2 = Pedido('678',[1,2])

p2.realizarPedido()

classPedido.pesquisaPedido("12874")

classPedido.excluiPedido("678")