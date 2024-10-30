from usuario.cadastrarUsuario import cadastrar_usuario
from usuario.listarUsuarios import listar_usuarios
from usuario.visualizarUsuario import visualizar_usuario
from usuario.atualizarUsuario import atualizar_usuario
from usuario.excluirUsuarios import excluir_usuario

def cliente_menu():
    menu = True
    while (menu):
        opcao_usuario = 11
        print("Menu do Usuário")
        print("1-Cadastrar usuário")
        print("2-Listar todos os usuários")
        print("3-Verificar dados de um usuário")
        print("4-Editar usuário")
        print("5-Deletar usuário")
        print("0-Voltar")
        opcao_usuario = input("Escolha uma opção: ")
        if (opcao_usuario == '1'):
            cadastrar_usuario()
            
        elif (opcao_usuario == '2'):
            listar_usuarios()
        
        elif (opcao_usuario == '3'):
            id = input("Insira o ID do usuário para ser visualizado: ")
            if (id):
                visualizar_usuario(id)
            else: 
                print("ID inválido")

        elif (opcao_usuario == '4'):
            listar_usuarios()
            id = input("Insira o ID do usuário para ser editado: ")
            if (id):
                atualizar_usuario(id)
            else:
                print("ID inválido")

        elif (opcao_usuario == '5'):
            listar_usuarios()
            id = input("Insira o ID do usuário para ser excluído: ")
            excluir_usuario(id)
        elif (opcao_usuario == '0'):
            menu = False
            return
        else:
            print("Opção inválida!")
        break