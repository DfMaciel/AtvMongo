from conexao import db
from vendedor.formatacaoVendedor import formatacao_vendedor

def listar_vendedores():
    print('Lista de vendedores: \n')
    global db
    mycol = db.vendedor
    resultado = mycol.find()
    for vendedor in resultado:
        formatacao_vendedor(vendedor)
        
    continuar = input("Pressione qualquer tecla para continuar...")
    if continuar:
        return

