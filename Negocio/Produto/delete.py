from helpers.utils import find_product

def delete_product(productId, productCol, sellerCol):
    product = find_product(productId, productCol)
    if product:
        productCol.delete_one({"_id": product["_id"]})

        vendedor_info = product.get("vendedor", {})
        if vendedor_info:
            sellerCol.update_one(
                {"_id": vendedor_info.get("_id")},
                {"$pull": {"produtos": {"produto": product["produto"]}}}
            )
        
        return print("Produto deletado com sucesso!")
    else:
        return print("Produto não encontrado!")
