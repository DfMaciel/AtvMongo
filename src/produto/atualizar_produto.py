from conexao import db
from bson import ObjectId
from bson.errors import InvalidId
from produto.formatacaoProduto import formatacao_produto

def atualizar_produto(id): 
    global db 
    mycol = db.produto
    try:
        myquery = {"_id": ObjectId(id)}
    except InvalidId:
        print("ID inválido")
        return
    resultado = mycol.find_one(myquery)
    if (resultado):
        print("Produto encontrado: ")
        formatacao_produto(resultado)
        editar = True
        while(editar):
            print('1 - Editar nome')
            print('2 - Editar descrição')
            print('3 - Editar Preço')
            print('4 - Editar Estoque')
            print('5 - Editar Marca')
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
                descricao = input("Descrição: ")
                if (descricao):
                    mycol.update_one(myquery, {"$set": {"descricao": descricao}})
                else:
                    print("Descrição inválida")
                    return
            elif (opcao == '3'):
                preco = input("Preço: ")
                if (preco):
                    mycol.update_one(myquery, {"$set": {"preco": preco}})
                else:
                    print("Preço inválida")
                    return
            elif (opcao == '4'):
                estoque = input("Estoque: ")
                if (estoque):
                    mycol.update_one(myquery, {"$set": {"estoque": estoque}})
                else:
                    print("Estoque inválida")
                    return
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
        print("Produto não encontrado")
        return