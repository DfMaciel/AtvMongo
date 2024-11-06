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
            print('5 - Editar produtos')
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
                        cep_escolhido = input("Qual o cep do endereço a ser removido?")
                        for endereco in resultado['endereco']:
                            if (endereco['cep'] == cep_escolhido):
                                resultado['endereco'].remove(endereco)
                                mycol.update_one(myquery, {"$set": {"endereco": resultado['endereco']}})
                                break
                            else:
                                print("Endereço não encontrado")
                                return
                    elif (opcao_endereco == '0'):
                        edicao_endereco = False
                        return
                    else:
                        print("Opção inválida")
                        return

            elif (opcao == '5'):
                print("Produtos do vendedor: ")
                print('-----------------')
                for produtos in resultado['produtos']:
                    for item in produtos:
                        print(item.capitalize(), ':', produtos[item])
                    print('-----------------')
                edicao_produto = True
                while(edicao_produto):
                    print("Qual opção você deseja realizar?")
                    print("1 - Adicionar produto")
                    print("2 - Remover produto")
                    print("0 - Voltar")
                    opcao_produto = input("Escolha uma opção: ")
                    if (opcao_produto == '1'):
                        continuar_produto = True
                        while (continuar_produto):
                            produto = input("Produto: ")
                            descricao = input("Descrição: ")
                            preco = input("Preço: ")
                            estoque = input("Estoque: ")
                            marca = input("Marca: ")
                            produto_inicial = {   
                                "produto":produto,
                                "descricao": descricao,
                                "preco": preco,
                                "estoque": estoque,
                                "marca": marca
                            }
                            resultado['produtos'].append(produto_inicial)
                            vendedor_produto = {
                                "nome": resultado['nome'],
                                "email": resultado['email'],
                                "endereco": resultado['endereco'],
                                "telefone": resultado['telefone'],
                            }
                            mycol2 = db.produto
                            mydoc2 = { "produto": produto, "descricao": descricao, "preco": preco, "estoque": estoque, "marca": marca, "vendedor": vendedor_produto}
                            x = mycol2.insert_one(mydoc2)
                            key = input("Deseja cadastrar um novo produto (S/N)? ")
                            if key in ['N', 'n']:
                                continuar_produto = False
                                mycol.update_one(myquery, {"$set": {"produtos": resultado['produtos']}})
                                break
                    if (opcao_produto == '2'):
                        produto_escolhido = input("Qual o nome do produto a ser excluido?")
                        for produto in resultado['produtos']:
                            if (produto['nome'] == produto_escolhido):
                                resultado['produtos'].remove(produto)
                                mycol.update_one(myquery, {"$set": {"produtos": resultado['produtos']}})
                                break
                            else:
                                print("Produto não encontrado")
                                return
                    if (opcao_produto == '0'):
                        edicao_produto = False
                        return
            elif (opcao == '0'):
                editar = False
                return
            else:
                print("Opção inválida")
    else:
        print("Usuário não encontrado")
        return