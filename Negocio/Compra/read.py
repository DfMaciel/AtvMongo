from helpers.utils import find_purchases
from bson import ObjectId

def read_purchase(nota_fiscal, purCol):
    print("\n")
    print("     Consultar Compra:")
    print("\n")
    purchase = find_purchases(nota_fiscal, purCol)

    if not purchase:
        return f"Compra com nota fiscal {nota_fiscal} não encontrada!"
    print("\n")
    print("     Detalhes da Compra:")
    print("\n")
    print(f"ID da Compra: {purchase['_id']}")
    print(f"Nota Fiscal: {purchase['nota_fiscal']}")
    print(f"Data da Compra: {purchase['data_compra']}")
    print(f"Usuário: {purchase['usuario']['nome']}")
    for index, product in enumerate(purchase["produtos"]):
        print(f"{index+1} - Produto: {product['produto']}, Marca: {product['marca']}, Quantidade: {product['quantidade']}")
    print(f"Endereço de Entrega: {purchase['endereco_entrega']['rua']}, {purchase['endereco_entrega']['numero']}")
    print(f"Valor Total: R$ {purchase['valor']:.2f}")
    print(f"Status: {purchase['status']}")
    print("\n")

def read_purchase_by_id(purchase_id, purCol):
    try:
        purchase = purCol.find_one({"_id": ObjectId(purchase_id)})
        if not purchase:
            print(f"Compra com ID {purchase_id} não encontrada!")
            return
        
        print("\n")
        print("     Detalhes da Compra:")
        print("\n")
        print(f"ID da Compra: {purchase['_id']}")
        print(f"Nota Fiscal: {purchase['nota_fiscal']}")
        print(f"Data da Compra: {purchase['data_compra']}")
        print(f"Usuário: {purchase['usuario']['nome']}")
        for index, product in enumerate(purchase["produtos"]):
            print(f"{index+1} - Produto: {product['produto']}, Marca: {product['marca']}, Quantidade: {product['quantidade']}")
        print(f"Endereço de Entrega: {purchase['endereco_entrega']['rua']}, {purchase['endereco_entrega']['numero']}")
        print(f"Valor Total: R$ {purchase['valor']:.2f}")
        print(f"Status: {purchase['status']}")
        print("\n")
    except Exception as e:
        print(f"Erro ao buscar compra: {e}")

def list_purchases(purCol):
    purchases = purCol.find().sort("data_compra", -1)
    purchases_list = list(purchases)
    
    if not purchases_list:
        print("Nenhuma compra encontrada.")
        return
        
    print("\nLista de Compras:")
    print("-" * 80)
    for purchase in purchases_list:
        print(f"ID: {purchase['_id']} | Nota Fiscal: {purchase['nota_fiscal']} | Cliente: {purchase['usuario']['nome']} | Valor: R$ {purchase['valor']:.2f} | Status: {purchase['status']}")
    print("-" * 80)
    
