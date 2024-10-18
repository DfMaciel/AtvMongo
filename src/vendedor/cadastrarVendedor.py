from conexao import db

def cadastrar_vendedor():
    global db
    mycol = db.vendedor
    print("\nInserindo um novo vendedor")
    nome = input("Nome: ")
    descricao = input("Descricao: ")
    preco = input("Preço: R$ ")
    estoque = input("Estoque: ")
    marca = input("Marca: ")
    continuar = True
    mydoc = { "nome": nome, "descricao": descricao, "preco": preco, "estoque": estoque, "marca": marca}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)