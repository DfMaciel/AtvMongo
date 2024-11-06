from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from usuario.formatacaoUsuario import formatacao_usuario
from produto.listarProdutos import listar_produtos

def atualizar_usuario(id):
    global db
    mycol = db.usuario
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
                edicao_endereco = True
                while (edicao_endereco):
                    print("Qual opção você deseja realizar?")
                    print("1 - Adicionar endereço")
                    print("2 - Remover endereço")
                    print("0 - Voltar")
                    opcao_endereco = input("Escolha uma opção: ")
                    if (opcao_endereco == '1'):
                        continuar = True
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
                    for item in favoritos:
                        print(item.capitalize(), ':', favoritos[item])
                    print('-----------------')
                edicao_favoritos = True
                while(edicao_favoritos):
                    print("Qual opção você deseja realizar?")
                    print("1 - Adicionar favorito")
                    print("2 - Remover favorito")
                    print("0 - Voltar")
                    opcao_favoritos = input("Escolha uma opção: ")
                    if (opcao_favoritos == '1'):
                        listar_produtos()
                        id_produto = input("Insira o ID do produto para ser adicionado: ")
                        if (id_produto):
                            myquery_produto = {"_id": ObjectId(id_produto)}
                            produto = db.produto.find_one(myquery_produto)
                            if (produto):
                                nome_vendedor = produto['vendedor']['nome']
                                produto_novo = {
                                    "_id": produto['_id'],
                                    "produto": produto['produto'],
                                    "preco": produto['preco'],
                                    "descricao": produto['descricao'],
                                    "estoque": produto['estoque'],
                                    "vendedor": nome_vendedor,
                                }
                                resultado['favoritos'].append(produto_novo)
                                mycol.update_one(myquery, {"$set": {"favoritos": resultado['favoritos']}})
                                print(f"Produto {produto['produto']} adicionado aos favoritos")
                            else:
                                print("Produto não encontrado")
                                return
                        else:
                            print("ID inválido")
                            return
                    elif (opcao_favoritos == 2):
                        id_produto = input("Insira o ID do produto para ser removido: ")
                        for favorito in resultado['favoritos']:
                            if (favorito['id'] == id_produto):
                                resultado['favoritos'].remove(favorito)
                                mycol.update_one(myquery, {"$set": {"favoritos": resultado['favoritos']}})
                                break
                    elif (opcao_favoritos == '0'):
                        edicao_favoritos = False
                        return
                    else:
                        print("Opção inválida")
                        return
            elif (opcao == '0'):
                editar = False
                return
            else:
                print("Opção inválida")
    else:
        print("Usuário não encontrado")
        return