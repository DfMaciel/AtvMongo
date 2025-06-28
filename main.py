from config import connection
from Menu.Produto.produto import manager_product
from Menu.Compra.compra import manager_purchase
from Menu.Usuario.usuario import manager_user
from Menu.Vendedor.vendedor import manager_seller

def main():
    db = connection()  
    if db is None:
        print("Erro ao conectar ao banco de dados.")
        return
    mercado_livre_db = db['Cluster0']  
    produto = mercado_livre_db['produto']
    usuario = mercado_livre_db['usuario']
    vendedor = mercado_livre_db['vendedor']
    compra = mercado_livre_db['compra']

    print("Bem vindo ao CRUD Mercado Livre")
    
    while True:
        print("Menu Principal")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Compras")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Vendedores")
        print("5 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue
        
        if opcao == 1:
            manager_product(produto, vendedor)
        elif opcao == 2:
            manager_purchase(usuario, produto, compras)
        elif opcao == 3:
            manager_user(usuario, produto)
        elif opcao == 4:
            manager_seller(vendedor)
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
