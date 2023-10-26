from Classes import *

n1 = Produtos("Notebook" , 4500)
n2 = Produtos("Iphone" , 8000)
n3 = Produtos("Tablet" , 2500)

Carrinho_Ana = Carrinho_Compra()

Carrinho_Ana.inserir_produto(n1)

Carrinho_Ana.inserir_produto(n1)
print(Carrinho_Ana.getLista(0).getNome())
print(Carrinho_Ana.getLista(0).getValor())

print("--------")

Carrinho_Ana.inserir_produto(n2)
Carrinho_Ana.inserir_produto(n2)
Carrinho_Ana.inserir_produto(n3)

Carrinho_Ana.listar_produtos()

print("-------")

Carrinho_Ana.delProduto(3)
Carrinho_Ana.listar_produtos()