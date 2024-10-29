from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from produto.formatacaoProduto import formatacao_produto

def visualizar_produto(id):
    global db
    mycol = db.produto
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Produto não encontrado")
        return
    else: 
        formatacao_produto(resultado)
        continuar = input("Pressione qualquer tecla para continuar...")
        if continuar:
            return