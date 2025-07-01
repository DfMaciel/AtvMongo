from Negocio.Vendedor.create import create_seller
from Negocio.Vendedor.read import read_seller, read_sellers
from Negocio.Vendedor.update import update_seller
from Negocio.Vendedor.delete import delete_seller

def manager_seller(collection):
    while True:
        print("\nGerenciamento de Vendedores")
        print("1 - Criar novo vendedor")
        print("2 - Ver vendedor específico")
        print("3 - Atualizar vendedor")
        print("4 - Deletar vendedor")
        print("5 - Lista de vendedores")
        print("6 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            create_seller(collection)
            input("\nPressione Enter para continuar...")
        elif opcao == 2:
            read_sellers(collection)
            input("\nPressione Enter para continuar...")
            seller_id = input("Digite o ID do vendedor que deseja ver: ")
            if seller_id:
                read_seller(seller_id, collection)
                input("\nPressione Enter para continuar...")
        elif opcao == 3:
            read_sellers(collection)
            input("\nPressione Enter para continuar...")
            seller_id = input("Digite o ID do vendedor que deseja atualizar: ")
            if seller_id:
                update_seller(seller_id, collection)
                input("\nPressione Enter para continuar...")
        elif opcao == 4:
            read_sellers(collection)
            input("\nPressione Enter para continuar...")
            seller_id = input("Digite o ID do vendedor que deseja deletar: ")
            if seller_id:
                delete_seller(seller_id, collection)
                input("\nPressione Enter para continuar...")
        elif opcao == 5:
            read_sellers(collection)
            input("\nPressione Enter para continuar...")
        elif opcao == 6:
            print("\n")
            print("Saindo do gerenciamento de vendedores.")
            break
        else:
            print("Opção inválida! Escolha novamente.")
