from conexao import db
from bson import ObjectId
from bson.errors import InvalidId

def excluir_usuario(id):
    global db
    mycol = db.usuario
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Usuário não encontrado")
        return
    else: 
        mydoc = mycol.delete_one(myquery)
        print("Usuário deletado")