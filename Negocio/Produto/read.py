from helpers.utils import find_product

def read_product(productId, productCol):
    product = find_product(productId, productCol)
    if product:
        print("\n")
        print("Informações do Produto:")
        print("\n")
        print(f"Produto: {product.get('produto', 'Informação não disponível')}")
        print(f"Descrição: {product.get('descricao', 'Informação não disponível')}")
        print(f"Marca: {product.get('marca', 'Informação não disponível')}")
        print(f"Preço: R$ {product.get('preco', 'Informação não disponível')}")
        print(f"Estoque: {product.get('estoque', 'Informação não disponível')}")
        
        vendedor = product.get('vendedor')
        if vendedor:
            print("\nInformações do Vendedor:")
            print(f"ID: {vendedor.get('_id', 'Informação não disponível')}")
            print(f"Nome: {vendedor.get('nome', 'Informação não disponível')}")
            print(f"E-mail: {vendedor.get('email', 'Informação não disponível')}")
            print(f"Telefone: {vendedor.get('telefone', 'Informação não disponível')}")
            
            print("\nEndereços do Vendedor:")
            for endereco in vendedor.get('endereco', []):
                print(f"  Rua: {endereco.get('rua')}")
                print(f"  Número: {endereco.get('numero')}")
                print(f"  Bairro: {endereco.get('bairro')}")
                print(f"  Cidade: {endereco.get('cidade')}")
                print(f"  Estado: {endereco.get('estado')}")
                print(f"  CEP: {endereco.get('cep')}")
                print()
    else: 
        return print("Produto não encontrado!")

def list_products(collection):
    mydoc = collection.find().sort("produto")
    products = list(mydoc)
    products_list = [{"id": str(product.get("_id")), "produto": product.get("produto"), "marca": product["marca"]} for product in products]
    print("\nLista de produtos:")
    print("-" * 60)
    for product in products_list:
        print(f"ID: {product['id']}")
        print(f"Produto: {product['produto']} - Marca: {product['marca']}")
        print("-" * 60)


    


