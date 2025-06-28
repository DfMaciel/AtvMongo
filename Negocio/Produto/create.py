def create_product(seller, productCol, sellerCol):
    print("\n")
    print("Inserindo um novo produto")
    print("\n")
    produto = input("Nome do produto: ")
    descricao = input("Descrição: ")
    marca = input("Marca: ")
    preco = input("Preço: ") 
    estoque = input("Estoque: ")  
    
    mydoc = {
        "produto": produto,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque,
        "marca": marca,
        "vendedor": {
            "_id": seller["_id"],
            "nome": seller["nome"],
            "email": seller["email"],
            "endereco": seller["endereco"],
            "telefone": seller["telefone"]
        }
    }
    result = productCol.insert_one(mydoc)
    product_id = result.inserted_id 
    
    seller_product = {
        "_id": product_id,
        "produto": produto,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque,
        "marca": marca
    }

    sellerCol.update_one({"_id": seller["_id"]}, {"$push": {"produtos": seller_product}})
    return print("Documento inserido com ID", product_id)

