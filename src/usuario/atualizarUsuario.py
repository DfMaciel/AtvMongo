from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from usuario.formatacaoUsuario import formatacao_usuario

def atualizar_usuario(id):
    global db
    mycol = db.produto
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    
    resultado = mycol.find_one(myquery)
    if (resultado):
        print("Usuário encontrado: ")
        formatacao_usuario(resultado)
        editar = True
        while(editar):
            print('1 - Editar nome')
            print('2 - Editar email')
            print('3 - Editar senha')
            print('4 - Editar endereço')
            print('5 - Editar favoritos')
            print('0 - Voltar')
            opcao = input("Escolha uma opção: ")
            if (opcao == '1'):
                nome = input("Nome: ")
                if (nome):
                    mycol.update_one(myquery, {"$set": {"nome": nome}})
                else:
                    print("Nome inválido")
                    return
            elif (opcao == '2'):
                email = input("Email: ")
                if (email):
                    mycol.update_one(myquery, {"$set": {"email": email}})
                else:
                    print("Email inválido")
                    return
            elif (opcao == '3'):
                senha = input("Senha: ")
                if (senha):
                    mycol.update_one(myquery, {"$set": {"senha": senha}})
                else:
                    print("Senha inválida")
                    return
            elif (opcao == '4'):
                print("Endereços do usuário: ")
                print('-----------------')
                for enderecos in resultado['endereco']:
                    for item in enderecos:
                        print(item.capitalize(), ':', enderecos[item])
                    print('-----------------')
                endereco_escolhido = input("Qual o cep do endereço a ser alterado?")
            

            elif (opcao == '5'):
                marca = input("Marca: ")
                if (marca):
                    mycol.update_one(myquery, {"$set": {"marca": marca}})
                else:
                    print("Marca inválida")
                    return
            elif (opcao == '0'):
                editar = False
                return
            else:
                print("Opção inválida")
    else:
        print("Usuário não encontrado")
        return