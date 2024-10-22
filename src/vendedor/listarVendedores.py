from conexao import db
from usuario.formatacaoUsuario import formatacao_usuario

def listar_vendedores():
    print('Lista de vendedores: \n')
    global db
    mycol = db.vendedor
    resultado = mycol.find()
    for usuario in resultado:
        formatacao_usuario(usuario)
        
    continuar = input("Pressione qualquer tecla para continuar...")
    if continuar:
        return

