from conexao import db
from bson import ObjectId

def excluir_vendedor(id):
    global db
    mycol = db.vendedor
    myquery = {"_id": ObjectId(id)}
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Vendedor não encontrado")
        return
    else: 
        mydoc = mycol.delete_one(myquery)
        print("Vendedor deletado")