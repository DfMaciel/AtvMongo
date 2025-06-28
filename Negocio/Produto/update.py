from helpers.utils import find_product

def update_product(productId, productCol, sellerCol):
    print("\n")
    print("Edição de Produto")
    print("\n")
    
    product = find_product(productId, productCol)
    if not product:
        print("Produto não encontrado!")
        return
    
    novo_preco = input("Mudar Preço (ou Enter para continuar): ")
    if novo_preco:
        product["preco"] = novo_preco
    
    novo_estoque = input("Mudar estoque (ou Enter para continuar): ")
    if novo_estoque:
        product["estoque"] = novo_estoque
    
    nova_descricao = input("Mudar descrição (ou Enter para continuar): ")
    if nova_descricao:
        product["descricao"] = nova_descricao
    
    # Atualizar no banco de produtos
    update_fields = {}
    if novo_preco:
        update_fields["preco"] = novo_preco
    if novo_estoque:
        update_fields["estoque"] = novo_estoque
    if nova_descricao:
        update_fields["descricao"] = nova_descricao
    
    if update_fields:
        productCol.update_one({"_id": product["_id"]}, {"$set": update_fields})
        
        # Atualizar no array de produtos do vendedor
        vendedor_id = product["vendedor"]["_id"] if "_id" in product["vendedor"] else None
        if vendedor_id:
            seller_update = {}
            if novo_preco:
                seller_update["produtos.$.preco"] = novo_preco
            if novo_estoque:
                seller_update["produtos.$.estoque"] = novo_estoque
            if nova_descricao:
                seller_update["produtos.$.descricao"] = nova_descricao
            
            sellerCol.update_one(
                {"_id": vendedor_id, "produtos.produto": product["produto"]}, 
                {"$set": seller_update}
            )
    
    print("\n")
    return print("Produto atualizado com sucesso!")

def update_sale_and_stock(product, quantity, productCol):
    try:
        stock = int(product.get("estoque", 0))
        if stock >= quantity:
            new_stock = stock - quantity
            productCol.update_one(
                {"_id": product["_id"]}, 
                {"$set": {"estoque": str(new_stock)}}
            )
            return True
        else:
            print("Estoque insuficiente!")
            return False
    except ValueError:
        print("Erro ao processar estoque!")
        return False
