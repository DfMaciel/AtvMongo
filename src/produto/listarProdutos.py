from conexao import db
from produto.formatacaoProduto import formatacao_produto

def listar_produtos():
    print('Lista de produtos: \n')
    global db
    mycol = db.produto
    resultado = mycol.find()
    for produto in resultado:
        formatacao_produto(produto)
        
    continuar = input("Pressione qualquer tecla para continuar...")
    if continuar:
        return

