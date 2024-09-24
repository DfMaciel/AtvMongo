from conexao import db
from bson import ObjectId

def excluir_produto():
    global db
    mycol = db.produto
    myquery = {"_id": ObjectId(id)}
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Produto não encontrado")
        return
    else: 
        mydoc = mycol.delete_one(myquery)
        print("Produto deletado")