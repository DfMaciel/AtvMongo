from helpers.utils import find_user
def read_user(id, usuarioCol):
    user = find_user(id, usuarioCol)
    if user:
        print("\n")
        print(f"ID: {user.get('_id')}")
        print(f"Nome: {user.get('nome')}")
        print(f"Email: {user.get('email')}")
        print(f"Senha: {user.get('senha')}")
        print("\n")
        print("Endereço(s):")
        print("\n")
        for endereco in user.get('endereco', []):

            print(f"  Rua: {endereco.get('rua')}")
            print(f"  Número: {endereco.get('numero')}")
            print(f"  Bairro: {endereco.get('bairro')}")
            print(f"  Cidade: {endereco.get('cidade')}")
            print(f"  Estado: {endereco.get('estado')}")
            print(f"  CEP: {endereco.get('cep')}")
        print("\n")
        
        if len(user.get("favoritos", [])) >= 1:
            print("Favoritos: ")
            print("\n")
            for index, product in enumerate(user["favoritos"]):
                nome_produto = product.get('nome', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                valor_produto = product.get('valor', 'N/A')
                print(f"    {index + 1} - Produto: {nome_produto}, Marca: {marca_produto}, Valor: R$ {valor_produto}")
                print("\n")
        else:
            print(f"Sua lista de favoritos está vazia.")
        if len(user.get("compras", [])) >= 1:
            print("\n")
            print("Compras: ")
            print("\n")
            for index, compra in enumerate(user["compras"]):
                print(f"    {index + 1} - Nota Fiscal: {compra.get('notaFiscal')}, Status: {compra.get('status')}, Valor Total: R$ {compra.get('valorTotal', 0.0):.2f}")
                for produto in compra.get("produtos", []):
                    print(f"        Produto: {produto.get('nome')}, Marca: {produto.get('marca')}, Quantidade: {produto.get('quantidade')}")
                print("\n")
        else:
            print("\n")
            print("Nenhuma compra registrada.")
    else:
        print("Usuario não encontrado!")

def read_users(usuariosCol):
    users = usuariosCol.find().sort("nome")
    users_list = [{"nome": user.get("nome"), "ID": user.get("_id")} for user in users]
    print("Lista de usuários:")
    for user in users_list:
        print(f"Nome: {user['nome']}, ID: {user['_id']}")
