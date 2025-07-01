from Negocio.Produto.create import create_product
from Negocio.Produto.update import update_product
from Negocio.Produto.read import read_product, list_products
from Negocio.Produto.delete import delete_product
from Negocio.Vendedor.read import read_sellers
from helpers.utils import find_seller

def manager_product(productCol, sellerCol):
    while True:
        print("\nGerenciamento de Produtos")
        print("1 - Criar novo produto")
        print("2 - Ver produto específico")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            read_sellers(sellerCol)
            input("\nPressione Enter para continuar...")
            seller_id = input("Digite o ID do vendedor: ")
            seller = find_seller(seller_id, sellerCol)
            if seller:
                create_product(seller, productCol, sellerCol)
                input("\nPressione Enter para continuar...")
            else:
                print("Vendedor não encontrado!")
                input("\nPressione Enter para continuar...")
        elif opcao == 2:
            list_products(productCol)
            input("\nPressione Enter para continuar...")
            product_id = str(input("Digite o ID do produto que deseja ver: "))
            if product_id:
                read_product(product_id, productCol)
                input("\nPressione Enter para continuar...")
        elif opcao == 3:
            list_products(productCol)
            input("\nPressione Enter para continuar...")
            product_id = str(input("Digite o ID do produto que deseja atualizar: "))
            if product_id:
                update_product(product_id, productCol, sellerCol)
                input("\nPressione Enter para continuar...")
        elif opcao == 4:
            list_products(productCol)
            input("\nPressione Enter para continuar...")
            product_id = str(input("Digite o ID do produto que deseja deletar: "))
            if product_id:
                delete_product(product_id, productCol, sellerCol)
                input("\nPressione Enter para continuar...")
        elif opcao == 5:
            print("Saindo do gerenciamento de produtos.")
            break
        else:
            print("Opção inválida! Escolha novamente.")
