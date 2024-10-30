from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from vendedor.formatacaoVendedor import formatacao_vendedor

def visualizar_vendedor(id):
    global db
    mycol = db.vendedor
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    resultado = mycol.find_one(myquery)
    if not resultado:
        print("Vendedor não encontrado")
        return
    else: 
        formatacao_vendedor(resultado)
        continuar = input("Pressione qualquer tecla para continuar...")
        if continuar:
            return