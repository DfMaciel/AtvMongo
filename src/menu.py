from usuario.cadastrarUsuario import cadastrar_usuario
from usuario.listarUsuarios import listar_usuarios
from usuario.visualizarUsuario import visualizar_usuario
from usuario.editarUsuario import atualizar_usuario

def menu ():
    entrada = 11
    sair = True

    while (sair):
        print("Sistema de CRUD Mercado Livre")
        print("1-Usuário")
        print("2-Produto")
        print("3-Vendedor")
        print("4-Compra")
        print("0-Sair")
        entrada = input("Escolha uma opção: ")

        if (entrada == '1'):
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

            #     elif (opcao_usuario == '5'):
            #         listar_usuarios()
            #         id = input("Insira o ID do usuário para ser excluído: ")
            #         excluir_usuario(id)
                elif (opcao_usuario == '0'):
                    menu = False
                    return
                else:
                    print("Opção inválida!")
                
        # elif (input == '2'):
        #     opcao_usuario = 11
        #     print("Menu do Vendedor")   
        #     print("1-Cadastrar vendedor")
        #     print("2-Listar todos os vendedores")
        #     print("3-Verificar dados de um vendedor")
        #     print("4-Editar vendedor")
        #     print("5-Deletar vendedor")
        #     print("0-Voltar")
        #     opcao_usuario = input("Escolha uma opção: ")
        #     if (opcao_usuario == '1'):
        #         cadastrar_vendedor()
                
        #     elif (opcao_usuario == '2'):
        #         listar_vendedores()
            
        #     elif (opcao_usuario == '3'):
        #         listar_vendedores()
        #         id = input("Insira o ID do vendedor para ser visualizado: ")
        #         visualizar_vendedor(id)

        #     elif (opcao_usuario == '4'):
        #         listar_vendedores()
        #         id = input("Insira o ID do vendedor para ser editado: ")
        #         atualizar_vendedor(id)

        #     elif (opcao_usuario == '5'):
        #         listar_vendedor()
        #         id = input("Insira o ID do vendedor para ser excluído: ")
        #         excluir_vendedor(id)
        #     elif (opcao_usuario == '0'):
        #         return
            
        # elif (input == '3'):
        #     opcao_usuario = 11
        #     print("Menu do Produto") 
        #     print("1-Cadastrar produto")
        #     print("2-Listar todos os produtos")
        #     print("3-Verificar dados de produto")
        #     print("4-Editar produto")
        #     print("5-Deletar produto") 
        #     print("0-Voltar")
        # elif (input == '4'):
        #     opcao_usuario = 11
        #     print("Menu de Compra")
        #     print("1-Realizar uma compra")
        #     print("2-Listar todas as compras")
        #     print("3-Editar uma compra")
        #     print("4-Excluir uma compra")
        #     print("0-Voltar")
        elif (input == '0'):
            sair = False
        else: 
            print("Opção inválida!")      

    print("Tchau Prof...")
