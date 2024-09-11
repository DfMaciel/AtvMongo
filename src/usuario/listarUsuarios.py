from conexao import db
from usuario.formatacaoUsuario import formatacao_usuario

def listar_usuarios():
    print('Lista de usuários: \n')
    global db
    mycol = db.usuario
    resultado = mycol.find()
    for usuario in resultado:
        formatacao_usuario(usuario)
        
    continuar = input("Pressione qualquer tecla para continuar...")
    if continuar:
        return

