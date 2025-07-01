from datetime import datetime
from bson import ObjectId
from helpers.utils import generate_nota_fical, find_user, find_product, calculate_final_value, list_addresses, register_address
from Negocio.Produto.read import list_products
from Negocio.Produto.update import update_sale_and_stock

def create_purchase(user, userCol, productCol, purchaseCol):
    print("\n     Inserindo uma nova compra\n")
    list_products(productCol)
    
    shopping_cart = []  
    value_purchase = 0 

    while True:
        product_id = input("Digite o ID do produto que deseja comprar: ")
        product = find_product(product_id, productCol)
        if not product:
            print("Produto não encontrado!")
            continue  
        
        quantity = int(input("Digite a quantidade que deseja comprar: "))
        shopping_cart.append({"product": product, "quantity": quantity})
        
        continue_process = input("Deseja selecionar mais algum produto? (S/N) ").lower()
        if continue_process == "n":
            break

    addresses = list_addresses(user)
    
    if not addresses:
        print("Registrar novo endereço de entrega:")
        print("\n")
        endereco = register_address(user["_id"], userCol, "USER")
        userCol.update_one({"_id": user["_id"]}, {"$push": {"endereco": endereco}})
        print("\n")
        print("Endereço cadastrado com sucesso!")
        user = find_user(user["_id"], userCol)
        addresses = list_addresses(user)

    print("\n")
    print("     Endereços disponíveis: ")
    print("\n")
    for index, address in enumerate(addresses):
        print(f"ID {index}. Rua: {address.get('rua')}, Número: {address.get('numero')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}")
    print("\n")
    
    delivery_address_id = int(input("Digite o ID do endereço de entrega: "))
    if delivery_address_id < 0 or delivery_address_id >= len(addresses):
        return print("Endereço de entrega inválido!")
    
    delivery_address_final = addresses[delivery_address_id]
    date_purchase = datetime.now()
    nota_fiscal = generate_nota_fical()

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        value_purchase += calculate_final_value(product, quantity)
        
    user_data = {
        "_id":user["_id"],
        "nome": user["nome"],
        "email": user["email"]
    }

    product_list = []
    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        
        product_data = {
            "_id": product["_id"],
            "produto": product["produto"],
            "descricao": product["descricao"],
            "preco": product["preco"],
            "quantidade": quantity,
            "marca": product["marca"],
            "vendedor": {
                "_id":product["vendedor"]["_id"],
                "nome": product["vendedor"]["nome"],
                "email": product["vendedor"]["email"],
                "telefone": product["vendedor"]["telefone"],
                "endereco": product["vendedor"]["endereco"]
            }
        }
        product_list.append(product_data)

    compra = {
        "valor": value_purchase,
        "data_compra": date_purchase,
        "status": "Processando",
        "nota_fiscal": nota_fiscal,
        "produtos": product_list,
        "endereco_entrega": delivery_address_final,
        "usuario": user_data
    }

    result = purchaseCol.insert_one(compra)
    purchase_id = result.inserted_id  
    compra_user = {
        "_id": purchase_id, 
        "valor": value_purchase,
        "data_compra": date_purchase,
        "status": "Processando",
        "produtos": product_list,
        "endereco_entrega": delivery_address_final
    }
    userCol.update_one({"_id": user["_id"]}, {"$push": {"compras": compra_user}})

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        update_sale_and_stock(product, quantity, productCol)
    print("\n")
    print(f"Documento inserido com ID {result.inserted_id}")
    print("\n")



