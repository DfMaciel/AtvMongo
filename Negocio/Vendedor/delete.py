from helpers.utils import find_seller

def delete_seller(seller_id, sellerCol):
    seller = find_seller(seller_id, sellerCol)
    if seller:
        sellerCol.delete_one({"_id": seller["_id"]})
        print("\n")
        return print("Vendedor deletado com sucesso!")
    return print("Vendedor não encontrado!")