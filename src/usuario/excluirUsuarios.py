from conexao import db
from bson import ObjectId

def excluir_usuario(id):
    global db
    mycol = db.usuario
    myquery = {"_id": ObjectId(id)}
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Usuário não encontrado")
        return
    else: 
        mydoc = mycol.delete_one(myquery)
        print("Usuário deletado")