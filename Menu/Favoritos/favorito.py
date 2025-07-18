from Negocio.Favorito.list import list_favorite
from Negocio.Favorito.add import add_favorite
from Negocio.Favorito.remove import remove_favorite
from helpers.utils import find_user

def manager_favorite(id, usuarioCol, produtoCol):
    user = find_user(id, usuarioCol)
    if not user:
        return print("Usuario não encontrado!")
    while True:
        print("\nGerenciamento de Favoritos")
        print("1 - Exibir favoritos")
        print("2 - Adicionar produto aos favoritos")
        print("3 - Remover produto dos favoritos")
        print("4 - Sair")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha um número entre 1 e 4.")
            continue
        
        if choice == 1:
            user = find_user(id, usuarioCol)
            list_favorite(user)
            input("\nPressione Enter para continuar...")
        elif choice == 2:
            user = find_user(id, usuarioCol)
            add_favorite(user, usuarioCol, produtoCol)
            input("\nPressione Enter para continuar...")
        elif choice == 3:
            user = find_user(id, usuarioCol)
            remove_favorite(user, usuarioCol, produtoCol)
            input("\nPressione Enter para continuar...") 
        elif choice == 4:
            print("Saindo dos favoritos.")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 4.")
