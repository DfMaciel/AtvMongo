from helpers.utils import find_seller

def read_seller(seller_id, sellerCol):
    seller = find_seller(seller_id, sellerCol)
    if seller:
        print("\n" + "="*50)
        print("INFORMAÇÕES DO VENDEDOR")
        print("="*50)
        print(f"ID: {seller.get('_id')}")
        print(f"Nome: {seller.get('nome')}")
        print(f"E-mail: {seller.get('email')}")
        print(f"Telefone: {seller.get('telefone')}")
        
        print("\nEndereços:")
        for index, endereco in enumerate(seller.get('endereco', []), 1):
            print(f"\n  Endereço {index}:")
            print(f"    {endereco.get('rua')}, {endereco.get('numero')}")
            print(f"    {endereco.get('bairro')}, {endereco.get('cidade')}")
            print(f"    {endereco.get('estado')}, CEP: {endereco.get('cep')}")
        
        if len(seller.get("produtos", [])) >= 1:
            print("\nProdutos:")
            for index, product in enumerate(seller["produtos"], 1):
                produto_nome = product.get('produto', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                preco_produto = product.get('preco', '0')
                estoque_produto = product.get('estoque', '0')
                print(f"  {index}. {produto_nome} - {marca_produto}")
                print(f"     Preço: R$ {preco_produto} | Estoque: {estoque_produto}")
        else:
            print("\nNenhum produto cadastrado.")
        print("="*50)
    else:
        print("Vendedor não encontrado!")

def read_sellers(sellerCol):
    sellers = sellerCol.find().sort("nome")
    sellers_list = [{"nome": seller.get("nome"), "ID": seller.get("_id")} for seller in sellers]
    print("\nLista de Vendedores:")
    print("-" * 50)
    if len(sellers_list) >= 1:
        for seller in sellers_list:
            print(f"Nome: {seller['nome']}")
            print(f"ID: {seller['ID']}")
            print("-" * 50)
    else:
        print("Sem Vendedores Cadastrados")
