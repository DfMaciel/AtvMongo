from Negocio.Compra.create import create_purchase
from Negocio.Compra.read import read_purchase, read_purchase_by_id, list_purchases
from Negocio.Compra.update import update_purchase
from Negocio.Compra.delete import delete_purchase
from Negocio.Usuario.read import read_users
from helpers.utils import find_user

def manager_purchase(userCol, productCol, purchaseCol):
    while True:
        print("\nGerenciamento de Compras")
        print("1 - Criar nova compra")
        print("2 - Ver compra específica")
        print("3 - Atualizar status da compra")
        print("4 - Deletar compra")
        print("5 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            read_users(userCol)
            input("\nPressione Enter para continuar...")
            user_id = input("Digite o ID do cliente para gerenciar suas compras: ")
            user = find_user(user_id, userCol)
            if not user:
                print("Usuário não encontrado!")
                input("\nPressione Enter para continuar...")
                continue
            create_purchase(user, userCol, productCol, purchaseCol)
            input("\nPressione Enter para continuar...")
        
        elif opcao == 2:
            list_purchases(purchaseCol)
            input("\nPressione Enter para continuar...")
            purchase_id = input("Digite o ID da compra que deseja ver: ")
            if purchase_id:
                read_purchase_by_id(purchase_id, purchaseCol)
                input("\nPressione Enter para continuar...")
        
        elif opcao == 3:
            list_purchases(purchaseCol)
            input("\nPressione Enter para continuar...")
            purchase_id = input("Digite o ID da compra que deseja atualizar: ")
            if purchase_id:
                # Para manter compatibilidade, ainda precisamos encontrar pela nota fiscal
                nota_fiscal = input("Digite a nota fiscal da compra: ")
                read_users(userCol)
                input("\nPressione Enter para continuar...")
                user_id = input("Digite o ID do cliente para atualizar a compra: ")
                user = find_user(user_id, userCol) 
                if user:
                    update_purchase(user, userCol, nota_fiscal, purchaseCol)
                    input("\nPressione Enter para continuar...")
                else:
                    print("Usuário não encontrado!")
                    input("\nPressione Enter para continuar...")
        
        elif opcao == 4:
            list_purchases(purchaseCol)
            input("\nPressione Enter para continuar...")
            purchase_id = input("Digite o ID da compra que deseja deletar: ")
            if purchase_id:
                # Para manter compatibilidade, ainda precisamos da nota fiscal
                nota_fiscal = input("Digite a nota fiscal da compra: ")
                read_users(userCol)
                input("\nPressione Enter para continuar...")
                user_id = input("Digite o ID do cliente para deletar a compra: ")
                user = find_user(user_id, userCol)  
                if user:
                    delete_purchase(user, userCol, nota_fiscal, purchaseCol)
                    input("\nPressione Enter para continuar...")
                else:
                    print("Usuário não encontrado!")
                    input("\nPressione Enter para continuar...")
        
        elif opcao == 5:
            print("Saindo do gerenciamento de compras.")
            break
        
        else:
            print("Opção inválida! Escolha novamente.")
