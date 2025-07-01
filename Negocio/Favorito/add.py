from Negocio.Produto.read import list_products
from helpers.utils import find_product

def add_favorite(user, userCol, productCol):
    list_products(productCol)
    favorites_list = []
    
    while True:
        product_id = input("Digite o ID do produto que deseja favoritar: ")
        product = find_product(product_id, productCol)
        
        if product:
            product_info = {
                "_id": product["_id"],
                "produto": product["produto"],
                "descricao": product["descricao"],
                "preco": product["preco"],
                "estoque": product["estoque"],
                "marca": product["marca"],
                "vendedor": {
                    "nome": product["vendedor"]["nome"],
                    "email": product["vendedor"]["email"],
                    "endereco": product["vendedor"]["endereco"],
                    "telefone": product["vendedor"]["telefone"]
                }
            }
            favorites_list.append(product_info)
        else:
            print("Produto não encontrado.")
        
        continuar = input("Deseja favoritar mais algum? (S/N): ").lower()
        if continuar == "n":
            break
    
    for fav in favorites_list:
        userCol.update_one(
            {"_id": user["_id"]},
            {"$push": {"favoritos": fav}}
        )
    print("\n")
    print("Favorito adicionados com sucesso.")



