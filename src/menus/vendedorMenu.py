from produto.cadastrarProduto import cadastrar_produto
from produto.listarProdutos import listar_produtos
from produto.visualizarProduto import visualizar_produto
from produto.atualizar_produto import atualizar_produto
from produto.excluirProduto import excluir_produto

def vendedor_menu():
    menu = True
    while (menu):
        opcao_usuario = 11
        print("Menu do vendedor")
        print("1-Cadastrar vendedor")
        print("2-Listar todos os vendedores")
        print("3-Verificar dados de um vendedor")
        print("4-Editar vendedor")
        print("5-Deletar vendedor")
        print("0-Voltar")
        opcao_usuario = input("Escolha uma opção: ")
        if (opcao_usuario == '1'):
            cadastrar_produto()
            
        elif (opcao_usuario == '2'):
            listar_produtos()
        
        elif (opcao_usuario == '3'):
            id = input("Insira o ID do produto para ser visualizado: ")
            if (id):
                visualizar_produto(id)
            else: 
                print("ID inválido")

        elif (opcao_usuario == '4'):
            listar_produtos()
            id = input("Insira o ID do produtos para ser editado: ")
            if (id):
                atualizar_produto(id)
            else:
                print("ID inválido")

        elif (opcao_usuario == '5'):
            listar_produtos()
            id = input("Insira o ID do usuário para ser excluído: ")
            excluir_produto(id)
            
        elif (opcao_usuario == '0'):
            menu = False
            return
        else:
            print("Opção inválida!")
        break