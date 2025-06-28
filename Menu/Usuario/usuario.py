from Negocio.Usuario.create import create_user
from Negocio.Usuario.read import read_user, read_users
from Negocio.Usuario.update import update_user
from Negocio.Usuario.delete import delete_user
from Menu.Favoritos.favorito import manager_favorite

def manager_user(usuarioCol, produtoCol):
    while True:
        print("1 - Criar novo usuario")
        print("2 - Ver usuario específico")
        print("3 - Atualizar usuario")
        print("4 - Deletar usuario")
        print("5 - Favoritos")
        print("6 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            create_user(usuarioCol)
        elif opcao == 2:
            read_users(usuarioCol)
            id = input("Digite a ID do usuario que deseja ver: ")
            if id:
                read_user(id, usuarioCol)
        elif opcao == 3:
            read_users(usuarioCol)
            id = input("Digite a ID do usuario que deseja atualizar: ")
            if id:
                update_user(id, usuarioCol)
        elif opcao == 4:
            id = input("Digite o id do usuario que deseja deletar: ")
            if id:
                delete_user(id, usuarioCol)
        elif opcao == 5:
            id = input("Digite o id do usuario que deseja ver os favoritos: ")
            if id:
                manager_favorite(id, usuarioCol, produtoCol)
        elif opcao == 6:
            print("Saindo do gerenciamento de usuario.")
            break
        else:
            print("Opção inválida! Escolha novamente.")


