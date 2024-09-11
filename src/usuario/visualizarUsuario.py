from conexao import db
from bson import ObjectId
from usuario.formatacaoUsuario import formatacao_usuario

def visualizar_usuario(id):
    global db
    mycol = db.usuario
    myquery = {"_id": ObjectId(id)}
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Usuário não encontrado")
        return
    else: 
        formatacao_usuario(resultado)
        continuar = input("Pressione qualquer tecla para continuar...")
        if continuar:
            return