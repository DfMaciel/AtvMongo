from helpers.utils import find_user
def read_user(id, usuarioCol):
    user = find_user(id, usuarioCol)
    if user:
        print("\n" + "="*50)
        print("INFORMAÇÕES DO USUÁRIO")
        print("="*50)
        print(f"ID: {user.get('_id')}")
        print(f"Nome: {user.get('nome')}")
        print(f"Email: {user.get('email')}")
        print(f"Senha: {user.get('senha')}")
        
        print("\nEndereços:")
        for i, endereco in enumerate(user.get('endereco', []), 1):
            print(f"\n  Endereço {i}:")
            print(f"    {endereco.get('rua')}, {endereco.get('numero')}")
            print(f"    {endereco.get('bairro')}, {endereco.get('cidade')}")
            print(f"    {endereco.get('estado')}, CEP: {endereco.get('cep')}")
        
        if len(user.get("favoritos", [])) >= 1:
            print("\nFavoritos:")
            for index, product in enumerate(user["favoritos"], 1):
                produto_nome = product.get('produto', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                preco_produto = product.get('preco', 'N/A')
                print(f"  {index}. {produto_nome} - {marca_produto} (R$ {preco_produto})")
        else:
            print("\nSua lista de favoritos está vazia.")
            
        if len(user.get("compras", [])) >= 1:
            print("\nCompras:")
            for index, compra in enumerate(user["compras"], 1):
                print(f"  {index}. ID: {compra.get('_id')}")
                print(f"     Status: {compra.get('status')} | Valor: R$ {compra.get('valor', 0.0):.2f}")
                for produto in compra.get("produtos", []):
                    print(f"     - {produto.get('produto')} ({produto.get('marca')}) x{produto.get('quantidade')}")
        else:
            print("\nNenhuma compra registrada.")
        print("="*50)
    else:
        print("Usuario não encontrado!")

def read_users(usuariosCol):
    users = usuariosCol.find().sort("nome")
    users_list = [{"nome": user.get("nome"), "ID": user.get("_id")} for user in users]
    print("\nLista de usuários:")
    print("-" * 50)
    for user in users_list:
        print(f"Nome: {user['nome']}")
        print(f"ID: {user['ID']}")
        print("-" * 50)
