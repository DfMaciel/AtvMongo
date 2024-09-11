from produto.cadastrarProduto import cadastrar_produto
from produto.listarProdutos import listar_produtos

def produto_menu():
    menu = True
    while (menu):
        opcao_usuario = 11
        print("Menu do produto")
        print("1-Cadastrar produto")
        print("2-Listar todos os produtos")
        print("3-Verificar dados de um produto")
        print("4-Editar produto")
        print("5-Deletar produto")
        print("0-Voltar")
        opcao_usuario = input("Escolha uma opção: ")
        if (opcao_usuario == '1'):
            cadastrar_produto()
            
        elif (opcao_usuario == '2'):
            listar_produtos()
        
        # elif (opcao_usuario == '3'):
        #     id = input("Insira o ID do usuário para ser visualizado: ")
        #     if (id):
        #         visualizar_usuario(id)
        #     else: 
        #         print("ID inválido")

        # elif (opcao_usuario == '4'):
        #     listar_usuarios()
        #     id = input("Insira o ID do usuário para ser editado: ")
        #     if (id):
        #         atualizar_usuario(id)
        #     else:
        #         print("ID inválido")

        # elif (opcao_usuario == '5'):
        #     listar_usuarios()
        #     id = input("Insira o ID do usuário para ser excluído: ")
        #     excluir_usuario(id)
        elif (opcao_usuario == '0'):
            menu = False
            return
        else:
            print("Opção inválida!")
        break