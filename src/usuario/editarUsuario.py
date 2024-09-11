from conexao import db
from bson import ObjectId
from usuario.formatacaoUsuario import formatacao_usuario

def atualizar_usuario(id):
    global db 
    mycol = db.usuario
    myquery = {"_id": ObjectId(id)}
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
                endereco = []
                continuar = True
                while (continuar):
                    rua = input("Rua: ")
                    numero = input("Num: ")
                    bairro = input("Bairro: ")
                    cidade = input("Cidade: ")
                    estado = input("Estado: ")
                    cep = input("CEP: ")
                    endereco_inicial = {   
                        "rua":rua,
                        "numero": numero,
                        "bairro": bairro,
                        "cidade": cidade,
                        "estado": estado,
                        "cep": cep
                    }
                    endereco.append(endereco_inicial)
                    key = input("Deseja cadastrar um novo endereço (S/N)? ")
                    if key.upper() == 'N':
                        mycol.update_one(myquery, {"$set": {"endereco": endereco}})
                        continuar = False
                        break
            # elif (opcao == '5'):
            #     favoritos = []
            #     continuar = True
            #     while (continuar):
            #         id_produto = input("ID do produto: ")
            #         favoritos.append(id_produto)
            #         key = input("Deseja cadastrar um novo favorito (S/N)? ")
            #         if key.upper == 'N':
            #             continuar = False
            #     myquery["favoritos"] = favoritos
            elif (opcao == '0'):
                editar = False
                return
            else:
                print("Opção inválida")
    else: 
        print("Usuário não encontrado")
        return
