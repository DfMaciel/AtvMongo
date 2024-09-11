from menus.clienteMenu import cliente_menu
from menus.produtoMenu import produto_menu

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
            cliente_menu()
                
        elif (entrada == '2'):
            produto_menu()
            
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
        elif (entrada == '0'):
            sair = False
            break
        else: 
            print("Opção inválida!")      

    print("Tchau Prof...")
