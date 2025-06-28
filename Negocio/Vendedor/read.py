from helpers.utils import find_seller

def read_seller(seller_id, sellerCol):
    seller = find_seller(seller_id, sellerCol)
    if seller:
        print("\n")
        print("Informações do vendedor: ")
        print(f"ID: {seller.get('_id')}")
        print(f"Nome: {seller.get('nome')}")
        print(f"E-mail: {seller.get('email')}")
        print(f"Telefone: {seller.get('telefone')}")
        print("\n")
        print("     Endereços:")
        print("\n")
        for endereco in seller.get('endereco', []):
            print(f"  Rua: {endereco.get('rua')}")
            print(f"  Número: {endereco.get('numero')}")
            print(f"  Bairro: {endereco.get('bairro')}")
            print(f"  Cidade: {endereco.get('cidade')}")
            print(f"  Estado: {endereco.get('estado')}")
            print(f"  CEP: {endereco.get('cep')}")
            print("\n")
        if len(seller.get("produtos", [])) >= 1:
            print("\n")
            print("     Produtos:")
            print("\n")
            for index, product in enumerate(seller["produtos"]):
                nome_produto = product.get('nome', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                valor_produto = product.get('valor', 'N/A')
                estoque_produto = product.get('estoque', 'N/A')
                vendas_produto = product.get('vendas', 'N/A')
                print(f"""   {index + 1} - Produto: {nome_produto}, Marca: {marca_produto}
                             Valor: R$ {valor_produto}, Estoque: {estoque_produto}, Vendas: {vendas_produto}""")
        else:
            print("Você não possui nenhum produto cadastrado.")
    else:
        return print("Vendedor não encontrado!")

def read_sellers(sellerCol):
    sellers = sellerCol.find().sort("nome")
    sellers_list = [{"nome": seller.get("nome"), "ID": seller.get("_id")} for seller in sellers]
    print("\n")
    print("     Lista de Vendedores:")
    print("\n")
    if len(sellers_list) >= 1:
        for seller in sellers_list:
            print(f"Nome: {seller['nome']}, ID: {seller['ID']}")
    else:
        return print("Sem Vendedores Cadastrados")
