from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from vendedor.formatacaoVendedor import formatacao_vendedor

def atualizar_vendedor(id):
    global db
    mycol = db.vendedor
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    
    resultado = mycol.find_one(myquery)
    if (resultado):
        print("Vendedor encontrado: ")
        formatacao_vendedor(resultado)
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
                edicao_endereco = True
                while (edicao_endereco):
                    print("Qual opção você deseja realizar?")
                    print("1 - Adicionar endereço")
                    print("2 - Remover endereço")
                    print("0 - Voltar")
                    opcao_endereco = input("Escolha uma opção: ")
                    if (opcao_endereco == '1'):
                        while (continuar):
                            lista_enderecos = resultado['endereco']
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
                            lista_enderecos.append(endereco_inicial)
                            key = input("Deseja cadastrar um novo endereço (S/N)? ")
                            if key in ['N', 'n']:
                                continuar = False
                                mycol.update_one(myquery, {"$set": {"endereco": lista_enderecos}})
                                break
                    elif (opcao_endereco == '2'):
                        cep_escolhido = input("Qual o cep do endereço a ser alterado?")
                        for endereco in resultado['endereco']:
                            if (endereco['cep'] == cep_escolhido):
                                resultado['endereco'].remove(endereco)
                                mycol.update_one(myquery, {"$set": {"endereco": resultado['endereco']}})
                                break
                    elif (opcao_endereco == '0'):
                        edicao_endereco = False
                        return
                    else:
                        print("Opção inválida")
                        return

            elif (opcao == '5'):
                print("Favoritos do usuário: ")
                print('-----------------')
                for favoritos in resultado['favoritos']:
                    for item in enderecos:
                        print(item.capitalize(), ':', enderecos[item])
                    print('-----------------')
                edicao_favoritos = True
                print("Qual opção você deseja realizar?")
                print("1 - Adicionar favorito")
                print("2 - Remover favorito")
                print("0 - Voltar")
            elif (opcao == '0'):
                editar = False
                return
            else:
                print("Opção inválida")
    else:
        print("Usuário não encontrado")
        return