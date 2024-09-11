from conexao import db

def cadastrar_produto():
    global db
    mycol = db.produto
    print("\nInserindo um novo produto")
    nome = input("Nome: ")
    descricao = input("Descricao: ")
    preco = input("Preço: R$ ")
    estoque = input("Estoque: ")
    marca = input("Marca: ")
    continuar = True
    # while (continuar):
    #     rua = input("Rua: ")
    #     numero = input("Num: ")
    #     bairro = input("Bairro: ")
    #     cidade = input("Cidade: ")
    #     estado = input("Estado: ")
    #     cep = input("CEP: ")
    #     endereco_inicial = {   
    #         "rua":rua,
    #         "numero": numero,
    #         "bairro": bairro,
    #         "cidade": cidade,
    #         "estado": estado,
    #         "cep": cep
    #     }
    #     endereco.append(endereco_inicial)
    #     key = input("Deseja cadastrar um novo endereço (S/N)? ")
    #     if key in ['N', 'n']:
    #         continuar = False
    #         break
    mydoc = { "nome": nome, "descricao": descricao, "preco": preco, "estoque": estoque, "marca": marca}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)