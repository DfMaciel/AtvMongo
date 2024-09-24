from conexao import db
from bson import ObjectId
from produto.formatacaoProduto import formatacao_produto

def visualizar_produto(id):
    global db
    mycol = db.produto
    myquery = {"_id": ObjectId(id)}
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Produto não encontrado")
        return
    else: 
        formatacao_produto(resultado)
        continuar = input("Pressione qualquer tecla para continuar...")
        if continuar:
            return